from django.db import models
from psqlextra.types import PostgresPartitioningMethod
from psqlextra.models import PostgresPartitionedModel


# https://django-postgres-extra.readthedocs.io/en/master/table_partitioning.html
class TempTest(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.RANGE
        key = ["timestamp"]

    name = models.TextField()
    timestamp = models.DateTimeField()


class MyModel(PostgresPartitionedModel):
    class PartitioningMeta:
        method = PostgresPartitioningMethod.LIST
        key = ["status"]

    name = models.TextField()
    timestamp = models.DateTimeField()
    status = models.BooleanField()


# from django.db import connection
# connection.schema_editor().add_list_partition(
#     model=MyModel,
#     name="pt1",
#     values=[True]
# )
# connection.schema_editor().add_list_partition(
#     model=MyModel,
#     name="pt2",
#     values=[False]
# )
