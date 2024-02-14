from fastapi.testclient import TestClient

from app import create_app
from views.course_views import get_all_courses

app = create_app()
client = TestClient(app) 


def test_get_all_courses():
    response = client.get('v1/courses')
    print(response.json())
    assert response.status_code == 200
    assert response.json() == [{'course_id': 'CSE101', 'course_name': 'Computer Science', 'course_credits': 3, 'course_discipline': 'Computer Science', 'date_of_entry': '2023-01-01'}]
