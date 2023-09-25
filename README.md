EXAMPLE

journal
```
-------- insert query
INSERT INTO import_journal(
        id,
        type_val,
        type_txt,
        date_val,
        date_txt,
        transaction_number_val,
        transaction_number_txt,
        document_number_val,
        document_number_txt,
        journal_purpose_val,
        journal_purpose_txt,
        journal_type_val,
        journal_type_txt,
        order_id_val,
        order_id_txt,
        entity_id_val,
        entity_id_txt,
        name_val,
        name_txt,
        account_val,
        account_txt,
        memo_val,
        memo_txt,
        department_val,
        department_txt,
        class_val,
        class_txt,
        item_val,
        item_txt,
        quantity_val,
        quantity_txt,
        currency_val,
        currency_txt,
        exchange_rate_val,
        exchange_rate_txt,
        amount_(debit)_val,
        amount_(debit)_txt,
        amount_(credit)_val,
        amount_(credit)_txt,
        amount_val,
        amount_txt,
        location_val,
        location_txt,
        shd_-_link_document_number_val,
        shd_-_link_document_number_txt,
        status_val,
        status_txt,
        created_by_val,
        created_by_txt,
        internal_id_val,
        internal_id_txt,
        line_id_val,
        line_id_txt,
        updated_at
) VALUES

-------- last insert query
 ON DUPLICATE KEY UPDATE
        type_val=VALUES(type_val),
        type_txt=VALUES(type_txt),
        date_val=VALUES(date_val),
        date_txt=VALUES(date_txt),
        transaction_number_val=VALUES(transaction_number_val),
        transaction_number_txt=VALUES(transaction_number_txt),
        document_number_val=VALUES(document_number_val),
        document_number_txt=VALUES(document_number_txt),
        journal_purpose_val=VALUES(journal_purpose_val),
        journal_purpose_txt=VALUES(journal_purpose_txt),
        journal_type_val=VALUES(journal_type_val),
        journal_type_txt=VALUES(journal_type_txt),
        order_id_val=VALUES(order_id_val),
        order_id_txt=VALUES(order_id_txt),
        entity_id_val=VALUES(entity_id_val),
        entity_id_txt=VALUES(entity_id_txt),
        name_val=VALUES(name_val),
        name_txt=VALUES(name_txt),
        account_val=VALUES(account_val),
        account_txt=VALUES(account_txt),
        memo_val=VALUES(memo_val),
        memo_txt=VALUES(memo_txt),
        department_val=VALUES(department_val),
        department_txt=VALUES(department_txt),
        class_val=VALUES(class_val),
        class_txt=VALUES(class_txt),
        item_val=VALUES(item_val),
        item_txt=VALUES(item_txt),
        quantity_val=VALUES(quantity_val),
        quantity_txt=VALUES(quantity_txt),
        currency_val=VALUES(currency_val),
        currency_txt=VALUES(currency_txt),
        exchange_rate_val=VALUES(exchange_rate_val),
        exchange_rate_txt=VALUES(exchange_rate_txt),
        amount_(debit)_val=VALUES(amount_(debit)_val),
        amount_(debit)_txt=VALUES(amount_(debit)_txt),
        amount_(credit)_val=VALUES(amount_(credit)_val),
        amount_(credit)_txt=VALUES(amount_(credit)_txt),
        amount_val=VALUES(amount_val),
        amount_txt=VALUES(amount_txt),
        location_val=VALUES(location_val),
        location_txt=VALUES(location_txt),
        shd_-_link_document_number_val=VALUES(shd_-_link_document_number_val),
        shd_-_link_document_number_txt=VALUES(shd_-_link_document_number_txt),
        status_val=VALUES(status_val),
        status_txt=VALUES(status_txt),
        created_by_val=VALUES(created_by_val),
        created_by_txt=VALUES(created_by_txt),
        internal_id_val=VALUES(internal_id_val),
        internal_id_txt=VALUES(internal_id_txt),
        line_id_val=VALUES(line_id_val),
        line_id_txt=VALUES(line_id_txt),
        updated_at=VALUES(updated_at)


-------- struct
TypeVal string   `json:"type_val"`
TypeTxt string   `json:"type_txt"`
DateVal string   `json:"date_val"`
DateTxt string   `json:"date_txt"`
TransactionNumberVal    string   `json:"transaction_number_val"`
TransactionNumberTxt    string   `json:"transaction_number_txt"`
DocumentNumberVal       string   `json:"document_number_val"`
DocumentNumberTxt       string   `json:"document_number_txt"`
JournalPurposeVal       string   `json:"journal_purpose_val"`
JournalPurposeTxt       string   `json:"journal_purpose_txt"`
JournalTypeVal  string   `json:"journal_type_val"`
JournalTypeTxt  string   `json:"journal_type_txt"`
OrderIdVal      string   `json:"order_id_val"`
OrderIdTxt      string   `json:"order_id_txt"`
EntityIdVal     string   `json:"entity_id_val"`
EntityIdTxt     string   `json:"entity_id_txt"`
NameVal string   `json:"name_val"`
NameTxt string   `json:"name_txt"`
AccountVal      string   `json:"account_val"`
AccountTxt      string   `json:"account_txt"`
MemoVal string   `json:"memo_val"`
MemoTxt string   `json:"memo_txt"`
DepartmentVal   string   `json:"department_val"`
DepartmentTxt   string   `json:"department_txt"`
ClassVal        string   `json:"class_val"`
ClassTxt        string   `json:"class_txt"`
ItemVal string   `json:"item_val"`
ItemTxt string   `json:"item_txt"`
QuantityVal     string   `json:"quantity_val"`
QuantityTxt     string   `json:"quantity_txt"`
CurrencyVal     string   `json:"currency_val"`
CurrencyTxt     string   `json:"currency_txt"`
ExchangeRateVal string   `json:"exchange_rate_val"`
ExchangeRateTxt string   `json:"exchange_rate_txt"`
Amount(Debit)Val        string   `json:"amount_(debit)_val"`
Amount(Debit)Txt        string   `json:"amount_(debit)_txt"`
Amount(Credit)Val       string   `json:"amount_(credit)_val"`
Amount(Credit)Txt       string   `json:"amount_(credit)_txt"`
AmountVal       string   `json:"amount_val"`
AmountTxt       string   `json:"amount_txt"`
LocationVal     string   `json:"location_val"`
LocationTxt     string   `json:"location_txt"`
Shd-LinkDocumentNumberVal       string   `json:"shd_-_link_document_number_val"`
Shd-LinkDocumentNumberTxt       string   `json:"shd_-_link_document_number_txt"`
StatusVal       string   `json:"status_val"`
StatusTxt       string   `json:"status_txt"`
CreatedByVal    string   `json:"created_by_val"`
CreatedByTxt    string   `json:"created_by_txt"`
InternalIdVal   string   `json:"internal_id_val"`
InternalIdTxt   string   `json:"internal_id_txt"`
LineIdVal       string   `json:"line_id_val"`
LineIdTxt       string   `json:"line_id_txt"`


-------- repo placeholder
(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)

-------- migration create
CREATE TABLE import_journal (
        id VARCHAR(255) PRIMARY KEY,
        type_val VARCHAR(255),
        type_txt VARCHAR(255),
        date_val VARCHAR(255),
        date_txt VARCHAR(255),
        transaction_number_val VARCHAR(255),
        transaction_number_txt VARCHAR(255),
        document_number_val VARCHAR(255),
        document_number_txt VARCHAR(255),
        journal_purpose_val VARCHAR(255),
        journal_purpose_txt VARCHAR(255),
        journal_type_val VARCHAR(255),
        journal_type_txt VARCHAR(255),
        order_id_val VARCHAR(255),
        order_id_txt VARCHAR(255),
        entity_id_val VARCHAR(255),
        entity_id_txt VARCHAR(255),
        name_val VARCHAR(255),
        name_txt VARCHAR(255),
        account_val VARCHAR(255),
        account_txt VARCHAR(255),
        memo_val VARCHAR(255),
        memo_txt VARCHAR(255),
        department_val VARCHAR(255),
        department_txt VARCHAR(255),
        class_val VARCHAR(255),
        class_txt VARCHAR(255),
        item_val VARCHAR(255),
        item_txt VARCHAR(255),
        quantity_val VARCHAR(255),
        quantity_txt VARCHAR(255),
        currency_val VARCHAR(255),
        currency_txt VARCHAR(255),
        exchange_rate_val VARCHAR(255),
        exchange_rate_txt VARCHAR(255),
        amount_(debit)_val VARCHAR(255),
        amount_(debit)_txt VARCHAR(255),
        amount_(credit)_val VARCHAR(255),
        amount_(credit)_txt VARCHAR(255),
        amount_val VARCHAR(255),
        amount_txt VARCHAR(255),
        location_val VARCHAR(255),
        location_txt VARCHAR(255),
        shd_-_link_document_number_val VARCHAR(255),
        shd_-_link_document_number_txt VARCHAR(255),
        status_val VARCHAR(255),
        status_txt VARCHAR(255),
        created_by_val VARCHAR(255),
        created_by_txt VARCHAR(255),
        internal_id_val VARCHAR(255),
        internal_id_txt VARCHAR(255),
        line_id_val VARCHAR(255),
        line_id_txt VARCHAR(255),
        updated_at DATETIME,
        meta_updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-------- reqRepo
req.Id,
req.TypeVal,
req.TypeTxt,
req.DateVal,
req.DateTxt,
req.TransactionNumberVal,
req.TransactionNumberTxt,
req.DocumentNumberVal,
req.DocumentNumberTxt,
req.JournalPurposeVal,
req.JournalPurposeTxt,
req.JournalTypeVal,
req.JournalTypeTxt,
req.OrderIdVal,
req.OrderIdTxt,
req.EntityIdVal,
req.EntityIdTxt,
req.NameVal,
req.NameTxt,
req.AccountVal,
req.AccountTxt,
req.MemoVal,
req.MemoTxt,
req.DepartmentVal,
req.DepartmentTxt,
req.ClassVal,
req.ClassTxt,
req.ItemVal,
req.ItemTxt,
req.QuantityVal,
req.QuantityTxt,
req.CurrencyVal,
req.CurrencyTxt,
req.ExchangeRateVal,
req.ExchangeRateTxt,
req.Amount(Debit)Val,
req.Amount(Debit)Txt,
req.Amount(Credit)Val,
req.Amount(Credit)Txt,
req.AmountVal,
req.AmountTxt,
req.LocationVal,
req.LocationTxt,
req.Shd-LinkDocumentNumberVal,
req.Shd-LinkDocumentNumberTxt,
req.StatusVal,
req.StatusTxt,
req.CreatedByVal,
req.CreatedByTxt,
req.InternalIdVal,
req.InternalIdTxt,
req.LineIdVal,
req.LineIdTxt,
req.UpdatedAt,


-------- ToModel
TypeVal:        b.TypeVal,
TypeTxt:        b.TypeTxt,
DateVal:        b.DateVal,
DateTxt:        b.DateTxt,
TransactionNumberVal:   b.TransactionNumberVal,
TransactionNumberTxt:   b.TransactionNumberTxt,
DocumentNumberVal:      b.DocumentNumberVal,
DocumentNumberTxt:      b.DocumentNumberTxt,
JournalPurposeVal:      b.JournalPurposeVal,
JournalPurposeTxt:      b.JournalPurposeTxt,
JournalTypeVal: b.JournalTypeVal,
JournalTypeTxt: b.JournalTypeTxt,
OrderIdVal:     b.OrderIdVal,
OrderIdTxt:     b.OrderIdTxt,
EntityIdVal:    b.EntityIdVal,
EntityIdTxt:    b.EntityIdTxt,
NameVal:        b.NameVal,
NameTxt:        b.NameTxt,
AccountVal:     b.AccountVal,
AccountTxt:     b.AccountTxt,
MemoVal:        b.MemoVal,
MemoTxt:        b.MemoTxt,
DepartmentVal:  b.DepartmentVal,
DepartmentTxt:  b.DepartmentTxt,
ClassVal:       b.ClassVal,
ClassTxt:       b.ClassTxt,
ItemVal:        b.ItemVal,
ItemTxt:        b.ItemTxt,
QuantityVal:    b.QuantityVal,
QuantityTxt:    b.QuantityTxt,
CurrencyVal:    b.CurrencyVal,
CurrencyTxt:    b.CurrencyTxt,
ExchangeRateVal:        b.ExchangeRateVal,
ExchangeRateTxt:        b.ExchangeRateTxt,
Amount(Debit)Val:       b.Amount(Debit)Val,
Amount(Debit)Txt:       b.Amount(Debit)Txt,
Amount(Credit)Val:      b.Amount(Credit)Val,
Amount(Credit)Txt:      b.Amount(Credit)Txt,
AmountVal:      b.AmountVal,
AmountTxt:      b.AmountTxt,
LocationVal:    b.LocationVal,
LocationTxt:    b.LocationTxt,
Shd-LinkDocumentNumberVal:      b.Shd-LinkDocumentNumberVal,
Shd-LinkDocumentNumberTxt:      b.Shd-LinkDocumentNumberTxt,
StatusVal:      b.StatusVal,
StatusTxt:      b.StatusTxt,
CreatedByVal:   b.CreatedByVal,
CreatedByTxt:   b.CreatedByTxt,
InternalIdVal:  b.InternalIdVal,
InternalIdTxt:  b.InternalIdTxt,
LineIdVal:      b.LineIdVal,
LineIdTxt:      b.LineIdTxt,
UpdatedAt:      null.TimeFrom(time.Now()),
```