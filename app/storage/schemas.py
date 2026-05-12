TABLES = ["contacts", "step_output", "events", "inbox", "audit_log", "bounces", "optout", "conversions"]
FILTER_OPS = {
    "string": ["equals", "not_equals", "contains", "not_contains", "starts_with", "ends_with", "is_empty", "is_not_empty"],
    "number": ["equals", "not_equals", "gt", "gte", "lt", "lte", "between"],
    "boolean": ["is_true", "is_false"],
    "date": ["equals", "before", "after", "between", "is_today", "is_last_n_days"],
    "enum": ["in", "not_in"],
    "array": ["contains", "not_contains", "size_gt", "size_lt", "is_empty"],
    "object": ["has_key", "path_equals"],
}
DEFAULT_SCHEMAS = {
    "contacts": ["contact_id", "email", "phone", "country", "audience_ids", "status", "created_at", "source_fields"],
    "step_output": ["step_id", "contact_id", "channel", "status", "sent_at", "delivered_at", "opened_at", "clicked_at", "provider_message_id"],
    "events": ["event_id", "provider", "channel", "event_type", "contact_id", "step_id", "created_at", "payload"],
    "inbox": ["msg_id", "channel", "contact_id", "from", "to", "body", "status", "received_at"],
    "audit_log": ["audit_id", "actor", "action", "resource", "created_at", "payload"],
    "bounces": ["bounce_id", "channel", "contact_id", "step_id", "reason", "created_at"],
    "optout": ["contact_id", "channel", "reason", "created_at"],
    "conversions": ["conversion_id", "contact_id", "country", "kind", "value", "created_at"],
}

def infer_type(value):
    if isinstance(value, bool): return "boolean"
    if isinstance(value, (int, float)): return "number"
    if isinstance(value, list): return "array"
    if isinstance(value, dict): return "object"
    text = str(value)
    if text.endswith("Z") or "T" in text and ":" in text: return "date"
    return "string"

def schema_for(table, rows):
    fields = list(DEFAULT_SCHEMAS.get(table, []))
    for row in rows:
        for key in row.keys():
            if key not in fields and key not in ("PartitionKey", "RowKey", "etag"):
                fields.append(key)
    return {"table": table, "fields": [{"field": f, "type": infer_type(next((r[f] for r in rows if f in r), "")), "filterable": f not in ("payload", "source_fields"), "sortable": f not in ("payload", "source_fields", "audience_ids"), "default_visible": f not in ("payload", "source_fields")} for f in fields], "filter_ops": FILTER_OPS}
