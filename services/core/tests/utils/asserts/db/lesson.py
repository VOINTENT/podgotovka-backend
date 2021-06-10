import datetime
from typing import Optional, List, Dict, Any

from tests.utils.asserts.utils import assert_json
from tests.utils.db import run_query


def assert_lesson_in_db(
        subject_id: Optional[int], course_id: Optional[int], name: Optional[str], description: Optional[str],
        youtube_link: Optional[str], time_start: Optional[datetime.datetime], time_finish: Optional[datetime.time],
        files: List[Dict[str, Any]], lecture: Optional[str]):
    result = run_query("""
        SELECT
            subject_id, course_id, name, description, youtube_link, time_start, time_finish, text
        FROM
            lesson
    """)[0]

    assert result['subject_id'] == subject_id
    assert result['course_id'] == course_id
    assert result['name'] == name
    assert result['description'] == description
    assert result['youtube_link'] == youtube_link

    if time_start is None:
        assert result['time_start'] is None
    else:
        assert result['time_start'].year == time_start.year and result['time_start'].month == time_start.month and result[
            'time_start'].day == time_start.day and result['time_start'].hour == time_start.hour and result[
                   'time_start'].minute == time_start.minute

    if time_finish is None:
        assert result['time_finish'] is None
    else:
        assert result['time_finish'].hour == time_finish.hour and result['time_finish'].minute == time_finish.minute

    if lecture is None:
        assert result['text'] is None
    else:
        assert_json(result['text'], lecture)

    # TODO: assert files
