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

siteSettings_Schema = [
  {
    "name": "activeViewOptOut",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  },
  {
    "name": "adBlockingOptOut",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  },
  {
    "name": "disableNewCookie",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  },
  [
    {
      "description": "",
      "name": "additionalKeyValues",
      "type": "STRING",
      "mode": "NULLABLE"
    },
    {
      "name": "includeClickThroughUrls",
      "type": "BOOLEAN",
      "mode": "NULLABLE"
    },
    {
      "name": "includeClickTracking",
      "type": "BOOLEAN",
      "mode": "NULLABLE"
    },
    {
      "description": "GENERATE_SEPARATE_TAG_FOR_EACH_KEYWORD, IGNORE, PLACEHOLDER_WITH_LIST_OF_KEYWORDS",
      "name": "keywordOption",
      "type": "STRING",
      "mode": "NULLABLE"
    }
  ],
  {
    "name": "videoActiveViewOptOutTemplate",
    "type": "BOOLEAN",
    "mode": "NULLABLE"
  },
  {
    "description": "BOTH, DEFAULT, FLASH, HTML5",
    "name": "vpaidAdapterChoiceTemplate",
    "type": "STRING",
    "mode": "NULLABLE"
  }
]
