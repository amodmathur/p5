import pytest

from types import SimpleNamespace
import random
import string

from flask_app.forms import SearchForm, MovieReviewForm
from flask_app.models import User, Review


def test_index(client):
    resp = client.get("/")
    assert resp.status_code == 200

    search = SimpleNamespace(search_query="guardians", submit="Search")
    form = SearchForm(formdata=None, obj=search)
    response = client.post("/", data=form.data, follow_redirects=True)

    assert b"Guardians of the Galaxy" in response.data


@pytest.mark.parametrize(
    ("query", "message"), 
    (
        ("", b"This field is required"),
        ("a", b"Too many results"),
        ("sadgagwe", b"Movie not found"),
        ('a' * 200, b"Field must be between 1 and 100 characters long.")
    )
)
def test_search_input_validation(client, query, message):
    response = client.get("/")
    assert response.status_code == 200

    search = SimpleNamespace(
        search_query=query,
        submit="Search"
    )
    form = SearchForm(formdata=None, obj=search)
    res = client.post(
        "/", data=form.data, follow_redirects=True
    )
    assert message in res.data



def test_movie_review(client, auth):
    guardians_id = "tt2015381"
    url = f"/movies/{guardians_id}"
    resp = client.get(url)

    assert resp.status_code == 200

    auth.register()
    res = auth.login()
    

    assert False


@pytest.mark.parametrize(
    ("movie_id", "message"), 
    (
    )
)
def test_movie_review_redirects(client, movie_id, message):
    assert False


@pytest.mark.parametrize(
    ("comment", "message"), 
    (
    )
)
def test_movie_review_input_validation(client, auth, comment, message):
    assert False
