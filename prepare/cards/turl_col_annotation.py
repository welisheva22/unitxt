from unitxt.blocks import (
    FormTask,
    InputOutputTemplate,
    LoadHF,
    SerializeTableAsIndexedRowMajor,
    TaskCard,
    TemplatesList,
)
from unitxt.catalog import add_to_catalog
from unitxt.test_utils.card import test_card

card = TaskCard(
    # TODO: hard-coded loading script path will have to be replaced
    loader=LoadHF(
        path="/Users/rajmohan/Downloads/turl_data/column_annotation_data_loader.py"
    ),
    preprocess_steps=[
        SerializeTableAsIndexedRowMajor(field_to_field=[["table", "table_lin"]])
    ],
    task=FormTask(
        inputs=["table_lin", "vocab", "colname"],
        outputs=["annotations"],
        metrics=["metrics.f1_micro"],
    ),
    templates=TemplatesList(
        [
            InputOutputTemplate(
                input_format="""
                    This is a column type annotation task.The goal for this task is to choose the correct types for one selected column of the table from the given candidates. Table: {table_lin};\n Selected Column: {colname}; \nCandidate Types: {vocab}; \nOutput:
                """.strip(),
                output_format="{annotations}",
            ),
        ]
    ),
)

test_card(card)
add_to_catalog(card, "cards.column_annotation", overwrite=True)
