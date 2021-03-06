# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['InterestTestCase::test_user_can_join_and_unjoin_social_club 1'] = {
    'data': {
        'joinSocialClub': {
            'joinedSocialClub': {
                'followerCategory': {
                    'description': 'For people who want to be happy.',
                    'id': 'Q2F0ZWdvcnlOb2RlOjI=',
                    'name': 'Python Meetup'
                },
                'id': 'SW50ZXJlc3ROb2RlOjQ='
            }
        }
    }
}

snapshots['InterestTestCase::test_user_can_join_and_unjoin_social_club 2'] = {
    'data': {
        'unJoinSocialClub': {
            'unjoinedSocialClub': {
                'followerCategory': {
                    'description': 'For people who want to be happy.',
                    'id': 'Q2F0ZWdvcnlOb2RlOjI=',
                    'name': 'Python Meetup'
                },
                'id': 'SW50ZXJlc3ROb2RlOk5vbmU='
            }
        }
    }
}

snapshots['InterestTestCase::test_user_cannot_unjoin_social_club_they_do_not_belong_to 1'] = {
    'data': {
        'unJoinSocialClub': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'The User @testuser2, has not joined Category : Python Meetup. ',
            'path': [
                'unJoinSocialClub'
            ]
        }
    ]
}

snapshots['InterestTestCase::test_user_can_join_and_unjoin_category 1'] = {
    'data': {
        'joinCategory': {
            'joinedCategory': {
                'followerCategory': {
                    'description': 'For people who want to be happy.',
                    'id': 'Q2F0ZWdvcnlOb2RlOjI=',
                    'name': 'Python Meetup'
                },
                'id': 'SW50ZXJlc3ROb2RlOjI4'
            }
        }
    }
}

snapshots['InterestTestCase::test_user_can_join_and_unjoin_category 2'] = {
    'data': {
        'unjoinCategory': {
            'unjoinedCategory': {
                'followerCategory': {
                    'description': 'For people who want to be happy.',
                    'id': 'Q2F0ZWdvcnlOb2RlOjI=',
                    'name': 'Python Meetup'
                },
                'id': 'SW50ZXJlc3ROb2RlOk5vbmU='
            }
        }
    }
}

snapshots['InterestTestCase::test_user_cannot_unjoin_category_they_do_not_belong_to 1'] = {
    'data': {
        'unjoinCategory': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'The User @testuser2, has not joined Category : Python Meetup. ',
            'path': [
                'unjoinCategory'
            ]
        }
    ]
}

snapshots['InterestTestCase::test_user_cannot_join_same_category_twice 1'] = {
    'data': {
        'joinCategory': None
    },
    'errors': [
        {
            'locations': [
                {
                    'column': 13,
                    'line': 3
                }
            ],
            'message': 'User has already shown interest in this category',
            'path': [
                'joinCategory'
            ]
        }
    ]
}
