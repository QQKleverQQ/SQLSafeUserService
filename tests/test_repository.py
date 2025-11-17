from app.repository import UserRepository

def test_create_user(test_db):
    repo = UserRepository(test_db)
    u = repo.create_user("alice", "pass")
    assert u.username == "alice"


def test_safe_query(test_db):
    repo = UserRepository(test_db)
    u = repo.create_user("bob", "123")
    row = repo.get_user_safe(u.id)
    assert row is not None


def test_unsafe_injection(test_db):
    repo = UserRepository(test_db)
    repo.create_user("admin", "x")
    # SQL injection attempt
    result = repo.get_user_unsafe("' OR '1'='1")
    assert len(result) >= 1
