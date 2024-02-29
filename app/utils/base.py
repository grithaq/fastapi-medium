from passlib.context import CryptContext


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def has_pass(password: str):
    return pwd_context.hash(password)


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

