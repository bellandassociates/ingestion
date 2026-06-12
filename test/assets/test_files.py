from datetime import date

csv_test_data = [
    ["name", "completed", "length_m", "sunk"],
    ["Titanic", date(1912,4,2), 269.1, True],
    ["Endurance", date(1912,12,17), 44, True],
    ["Emma Maersk", date(2006,5,18), 398, False],
]

csv_test_schema = {
    "database": "sample_data",
    "tables": {
        "ships": {
            "orientation": "h",
            "columns": {
                "name": "string",
                "completed": "date",
                "length_m": "float",
                "sunk": "boolean",
            },
        },
    },
}


xlsx_test_workbook = {
    "Ships": [
        ["name", "completed", "length_m", "sunk"],
        ["Titanic", date(1912,4,2), 269.1, True],
        ["Endurance", date(1912,12,17), 44, True],
        ["Emma Maersk", date(2006,5,18), 398, False],
    ],
    "Legos": [
        ["Set Types", "Ships"],
        ["Total price", 679.99+269.99+149.99],
        [],
        ["Set number", "Set Name", "Price", "Pieces"],
        [10294, "Titanic", 679.99, 9090],
        [10335, "Endurance", 269.99, 3011],
        [40955, "Ane Maersk", 149.99, 1516],
    ]
}

xlsx_test_schema = {
    "database": "sample_data",
    "sheets": {
        "Ships": {
            "tables": {
                "ships": {
                    "orientation": "h",
                    "columns": {
                        "name": "string",
                        "completed": "date",
                        "length_m": "float",
                        "sunk": "boolean",
                    },
                },
            },
        },
        "Legos": {
            "tables": {
                "lego_header": {
                    "orientation": "v",
                    "columns": {
                        "Set Types": "string",
                        "Total price": "decimal"
                    },
                },
                "lego": {
                    "orientation": "h",
                    "columns": {
                        "Set number": "int",
                        "Set name": "string",
                        "Price": "decimal",
                        "Pieces": "int",
                    },
                },
            },
        },
    },
}

# EOF
