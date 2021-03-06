###########################################################################
#
#  Copyright 2019 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

advertiserLandingPagesListResponse_Schema = [
  {
    "description": "",
    "name": "kind",
    "type": "STRING",
    "mode": "NULLABLE"
  },
  {
    "name": "landingPages",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {
        "description": "",
        "name": "advertiserId",
        "type": "INT64",
        "mode": "NULLABLE"
      },
      {
        "name": "archived",
        "type": "BOOLEAN",
        "mode": "NULLABLE"
      },
      {
        "name": "deepLinks",
        "type": "RECORD",
        "mode": "REPEATED",
        "fields": [
          {
            "description": "",
            "name": "appUrl",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "description": "",
            "name": "fallbackUrl",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "description": "",
            "name": "kind",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          [
            {
              "description": "APPLE_APP_STORE, GOOGLE_PLAY_STORE, UNKNOWN",
              "name": "directory",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "description": "",
              "name": "id",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "description": "",
              "name": "kind",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "description": "",
              "name": "publisherName",
              "type": "STRING",
              "mode": "NULLABLE"
            },
            {
              "description": "",
              "name": "title",
              "type": "STRING",
              "mode": "NULLABLE"
            }
          ],
          {
            "name": "remarketingListIds",
            "type": "INT64",
            "mode": "REPEATED"
          }
        ]
      },
      {
        "description": "",
        "name": "id",
        "type": "INT64",
        "mode": "NULLABLE"
      },
      {
        "description": "",
        "name": "kind",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "description": "",
        "name": "name",
        "type": "STRING",
        "mode": "NULLABLE"
      },
      {
        "description": "",
        "name": "url",
        "type": "STRING",
        "mode": "NULLABLE"
      }
    ]
  },
  {
    "description": "",
    "name": "nextPageToken",
    "type": "STRING",
    "mode": "NULLABLE"
  }
]
