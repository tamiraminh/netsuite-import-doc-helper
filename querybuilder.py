column = ["type_val", "type_txt", "date_val", "date_txt", "transaction_number_val", "transaction_number_txt", "document_number_val", "document_number_txt", "journal_purpose_val", "journal_purpose_txt", "journal_type_val", "journal_type_txt", "order_id_val", "order_id_txt", "entity_id_val", "entity_id_txt", "name_val", "name_txt", "account_val", "account_txt", "memo_val", "memo_txt", "department_val", "department_txt", "class_val", "class_txt", "item_val",
          "item_txt", "quantity_val", "quantity_txt", "currency_val", "currency_txt", "exchange_rate_val", "exchange_rate_txt", "amount_(debit)_val", "amount_(debit)_txt", "amount_(credit)_val", "amount_(credit)_txt", "amount_val", "amount_txt", "location_val", "location_txt", "shd_-_link_document_number_val", "shd_-_link_document_number_txt", "status_val", "status_txt", "created_by_val", "created_by_txt", "internal_id_val", "internal_id_txt", "line_id_val", "line_id_txt"]


def insertQuery(array, dbname):
    result = "INSERT INTO " + "import_" + dbname + "(\n \tid,\n"
    for i in range(len(array)):
        result += "\t" + array[i] + ",\n"
    result += "\tupdated_at\n"

    result += ") VALUES "

    print(result)


def lastInsertQuery(array):
    result = " ON DUPLICATE KEY UPDATE \n"
    for i in range(len(array)):
        result += "\t" + array[i] + "=VALUES(" + array[i] + "),\n"
    result += "\tupdated_at=VALUES(updated_at)\n"
    print(result)


def buildstruct(array, dborjson):
    result = ""
    for i in range(len(array)):
        katas = array[i].split("_")
        kata = ""
        for j in range(len(katas)):
            kata += katas[j].title()
        result += kata + "\t" + "string \t" + " `" + \
            dborjson + ":\"" + array[i] + "\"`\n"
    print(result)


def placeholder(array):
    result = "(?,"
    for i in range(len(array)):
        if i == (len(array) - 1):
            # two because of updated at
            result += "?,?)"
            break
        result += "?,"
    print(result)


def migrationCreate(array, dbname):
    result = "CREATE TABLE " + "import_" + dbname + \
        " (\n \tid VARCHAR(255) PRIMARY KEY,\n"
    for i in range(len(array)):
        result += "\t" + array[i] + " VARCHAR(255),\n"
    result += "\tupdated_at DATETIME,\n"
    result += "\tmeta_updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP\n);"
    print(result)


def reqRepo(array):
    result = "req.Id,\n"
    for i in range(len(array)):
        katas = array[i].split("_")
        kata = ""
        for j in range(len(katas)):
            kata += katas[j].title()
        result += "req." + kata + ",\n"
    result += "req.UpdatedAt,\n"
    print(result)


def toModel(array):
    result = ""
    for i in range(len(array)):
        katas = array[i].split("_")
        kata = ""
        for j in range(len(katas)):
            kata += katas[j].title()
        result += kata + ":\t" + "b." + kata + ",\n"
    result += "UpdatedAt:\t" + "null.TimeFrom(time.Now()),"
    print(result)


print("-------- insert query")
insertQuery(column, "journal")
print("\n-------- last insert query")
lastInsertQuery(column)
print("\n-------- struct")
buildstruct(column, "json")
print("\n-------- repo placeholder")
placeholder(column)
print("\n-------- migration create")
migrationCreate(column, "journal")
print("\n-------- reqRepo")
reqRepo(column)
print("\n-------- ToModel")
toModel(column)
