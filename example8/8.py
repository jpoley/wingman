# Import the necessary dbt modules
from dbt import utils
from dbt.adapters import postgres
from dbt.adapters.postgres import PostgresConnectionManager
from dbt.task.base import BaseTask
from dbt.task.run import RunTask
from dbt.task.test import TestTask
from dbt.task.compile import CompileTask
from dbt.task.clean import CleanTask
from dbt.task.debug import DebugTask
from dbt.task.deps import DepsTask
from dbt.task.docs import DocsTask
from dbt.task.list import ListTask
from dbt.task.rpc import RPCTask
from dbt.task.seed import SeedTask
from dbt.task.snapshot import SnapshotTask
from dbt.task.source import SourceTask
from dbt.task.version import VersionTask
from dbt.task.generate import GenerateTask
from dbt.task.run_operation import RunOperationTask
from dbt.task.run_sql import RunSQLTask
from dbt.task.compile_sql import CompileSQLTask
from dbt.task.run_hooks import RunHooksTask
from dbt.task.generate_docs import GenerateDocsTask
from dbt.task.generate_schema import GenerateSchemaTask
from dbt.task.generate_source import GenerateSourceTask
from dbt.task.generate_test import GenerateTestTask
from dbt.task.generate_model import GenerateModelTask
from dbt.task.generate_snapshot import GenerateSnapshotTask
from dbt.task.generate_seed import GenerateSeedTask
from dbt.task.generate_archive import GenerateArchiveTask
from dbt.task.generate_macro import GenerateMacroTask
from dbt.task.generate_analysis import GenerateAnalysisTask
from dbt.task.generate_exposure import GenerateExposureTask
from dbt.task.generate_run_operation import GenerateRunOperationTask
from dbt.task.generate_run_sql import GenerateRunSQLTask
from dbt.task.generate_compile_sql import GenerateCompileSQLTask
from dbt.task.generate_run_hooks import GenerateRunHooksTask
from dbt.task.generate_generate_docs import GenerateGenerateDocsTask
from dbt.task.generate_generate_schema import GenerateGenerateSchemaTask
from dbt.task.generate_generate_source import GenerateGenerateSourceTask
from dbt.task.generate_generate_test import GenerateGenerateTestTask
from dbt.task.generate_generate_model import GenerateGenerateModelTask
from dbt.task.generate_generate_snapshot import GenerateGenerateSnapshotTask
from dbt.task.generate_generate_seed import GenerateGenerateSeedTask
from dbt.task.generate_generate_archive import GenerateGenerateArchiveTask
from dbt.task.generate_generate_macro import GenerateGenerateMacroTask
from dbt.task.generate_generate_analysis import GenerateGenerateAnalysisTask
from dbt.task.generate_generate_exposure import GenerateGenerateExposureTask
from dbt.task.generate_generate_run_operation import GenerateGenerateRunOperationTask
from dbt.task.generate_generate_run_sql import GenerateGenerateRunSQLTask
from dbt.task.generate_generate_compile_sql import GenerateGenerateCompileSQLTask
from dbt.task.generate_generate_run_hooks import GenerateGenerateRunHooksTask

# Define the borrower model
borrower_model = """
    select
        borrower_id,
        first_name,
        last_name,
        address,
        phone_number
    from
        borrowers
"""

# Define the transform step
transform_step = """
    select
        borrower_id,
        concat(first_name, ' ', last_name) as full_name,
        address,
        phone_number
    from
        borrower_model
"""

# Run the dbt Labs job
def run_dbt_job():
    # Connect to the database
    connection = PostgresConnectionManager()

    # Compile the borrower model
    compiled_borrower_model = connection.compile_sql(borrower_model)

    # Run the borrower model
    connection.execute(compiled_borrower_model)

    # Compile the transform step
    compiled_transform_step = connection.compile_sql(transform_step)

    # Run the transform step
    connection.execute(compiled_transform_step)

# Call the function to run the dbt Labs job
run_dbt_job()
