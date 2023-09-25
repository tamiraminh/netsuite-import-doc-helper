column = ["record_type", "result_id", "internal_id_val", "internal_id_txt", "type_val", "type_txt", "date_val", "date_txt", "transaction_number_val", "transaction_number_txt", "document_number_val", "document_number_txt", "bill_type_val", "bill_type_txt", "vendor_name_val", "vendor_name_txt", "no_inv_vendor_val", "no_inv_vendor_txt", "account_val", "account_txt", "department_val", "department_txt", "class_val", "class_txt", "currency_val", "currency_txt", "exchange_rate_val", "exchange_rate_txt", "item_val", "item_txt", "item_name_val", "item_name_txt", "quantity_val", "quantity_txt", "debit__val",
          "debit__txt", "credit_val", "credit_txt", "amount_val", "amount_txt", "tax_code_(vat)_val", "tax_code_(vat)_txt", "wht_code_val", "wht_code_txt", "wht_rate_val", "wht_rate_txt", "wht_amount_val", "wht_amount_txt", "memo_val", "memo_txt", "location_val", "location_txt", "expense_category_val", "expense_category_txt", "related_to_doc_number_val", "related_to_doc_number_txt", "amount_paid_val", "amount_paid_txt", "terms_val", "terms_txt", "due_date_val", "due_date_txt", "status_val", "status_txt", "created_by_val", "created_by_txt", "created_from_val", "created_from_txt", "line_id_val", "line_id_txt"]


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
