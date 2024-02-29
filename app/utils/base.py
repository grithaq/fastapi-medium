def paginate(items, page, per_page):
    start = (page - 1) * per_page
    end = start + per_page
    current = page
    total = len(items)
    data = {
        "current": current,
        "total": total,
        "items": items[start:end]
    }
    return data