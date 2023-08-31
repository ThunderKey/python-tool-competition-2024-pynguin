"""A test generator using Pynguin."""
import os
import tempfile

import pynguin.configuration as config
import pynguin.generator as pynguin

from python_tool_competition_2024.generation_results import (
    FailureReason,
    TestGenerationFailure,
    TestGenerationResult,
    TestGenerationSuccess,
)
from python_tool_competition_2024.generators import FileInfo, TestGenerator


class PynguinTestGenerator(TestGenerator):
    """A test generator using Pynguin."""

    def build_test(self, target_file_info: FileInfo) -> TestGenerationResult:
        """Generate a test for the specific target file.

        Args:
            target_file_info: The `FileInfo` of the file to generate a test for.

        Returns:
            Either a `TestGenerationSuccess` if it was successful, or a
            `TestGenerationFailure` otherwise.
        """
        with tempfile.TemporaryDirectory() as tempdir:
            _set_pynguin_configuration(tempdir, target_file_info)
            try:
                pynguin_result = pynguin.run_pynguin()
            except BaseException as e:
                return TestGenerationFailure((e,), FailureReason.UNEXPECTED_ERROR)

            if pynguin_result == pynguin.ReturnCode.OK:
                return TestGenerationSuccess(
                    _read_generated_tests(tempdir, target_file_info)
                )
            elif pynguin_result == pynguin.ReturnCode.NO_TESTS_GENERATED:
                return TestGenerationFailure(
                    ("Pynguin did not generate any tests.",),
                    FailureReason.NOTHING_GENERATED,
                )
            else:
                return TestGenerationFailure(
                    (
                        "Incorrect configuration of Pynguin.",
                        "Please check its configuration settings.",
                    ),
                    FailureReason.UNSUPPORTED_FEATURE_USED,
                )



def _set_pynguin_configuration(tempdir: str, target_file_info: FileInfo) -> None:
    pynguin_config = config.Configuration(
        project_path=str(target_file_info.config.targets_dir),
        module_name=target_file_info.module_name,
        test_case_output=config.TestCaseOutputConfiguration(
            output_path=tempdir,
        ),
    )
    pynguin.set_configuration(pynguin_config)


def _read_generated_tests(tempdir: str, target_file_info: FileInfo) -> str:
    module_name = target_file_info.module_name.replace(".", "_")
    test_file_name = f"test_{module_name}.py"
    with open(os.path.join(tempdir, test_file_name)) as f:
        return f.read()
