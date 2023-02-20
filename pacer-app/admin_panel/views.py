from django.shortcuts import render
from django.db import connection
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

import sqlparse
from sql_metadata import Parser

from .forms import SQLQueryForm


class AdminPanelView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, *args, **kwargs):
        form = SQLQueryForm()
        context = {
            "form": form
        }
        return render(request, "admin_panel/sql_queryer.html", context)

    def post(self, request, *args, **kwargs):
        form = SQLQueryForm(request.POST)
        if form.is_valid():
            sql_query = form.cleaned_data["sql_query"]
            # If there are multiple statements only take the last one
            statement = sqlparse.parse(sql_query)[-1]
            stmt_type = statement.get_type()
            if stmt_type == "UNKNOWN":
                context = {
                    "form": form,
                    "message": ("error", "Not a valid query")
                }
                return render(request, "admin_panel/sql_queryer.html", context)

            user = request.user
            sql_val = Parser(sql_query)
            try:
                table_names = sql_val.tables
            except ValueError:
                context = {
                    "form": form,
                    "message": ("error", "Not a valid query")
                }
                return render(request, "admin_panel/sql_queryer.html", context)

            # If user queries from multiple tables and one of them is not authorized,
            # fail the query
            has_perms = [False] * len(table_names)
            for i in range(len(table_names)):
                table_name = table_names[i]
                if stmt_type == "SELECT" and user.has_perm(f"{table_name}.view_{table_name}"):
                    has_perms[i] = True
                elif stmt_type == "UPDATE" and user.has_perm(f"{table_name}.change_{table_name}"):
                    has_perms[i] = True

            if all(has_perms) == True:
                context = self.run_query(str(statement), stmt_type, form)
            else:
                context = {
                    "form": form,
                    "message": ("error", "Not authorized to run the query")
                }

            return render(request, "admin_panel/sql_queryer.html", context)

    def run_query(self, query, stmt_type, form):
        res = {}
        with connection.cursor() as cursor:
            try:
                cursor.execute(query)
                if stmt_type == "SELECT":
                    res = {
                        "form": form,
                        "message": ("success", "Query successful"),
                        "columns": [col[0] for col in cursor.description],
                        "rows": [item for item in cursor.fetchall()]
                    }
                elif stmt_type == "UPDATE":
                    res = {
                        "form": form,
                        "message": ("success", "Query successful")
                    }
            except Exception as e:
                res = {
                    "form": form,
                    "message": ("error", str(e))
                }
        return res