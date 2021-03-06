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

'''
--------------------------------------------------------------

Before running this Airflow module...

  Install StarThinker in cloud composer from open source: 

    pip install git+https://github.com/google/starthinker

  Or push local code to the cloud composer plugins directory:

    source install/deploy.sh
    4) Composer Menu	   
    l) Install All

--------------------------------------------------------------

Archive

Wipe old information from a Storage bucket based on last update time.

Specify how many days back to retain data and which buckets and paths to purge.
Everything under a path will be moved to archive or deleted depending on your choice.

'''

from starthinker_airflow.factory import DAG_Factory
 
# Add the following credentials to your Airflow configuration.
USER_CONN_ID = "starthinker_user" # The connection to use for user authentication.
GCP_CONN_ID = "starthinker_service" # The connection to use for service authentication.

INPUTS = {
  'auth_write': 'service',  # Credentials used for writing data.
  'archive_days': 7,
  'archive_bucket': '',
  'archive_path': '',
  'archive_delete': False,
}

TASKS = [
  {
    'archive': {
      'auth': {
        'field': {
          'name': 'auth_write',
          'kind': 'authentication',
          'order': 1,
          'default': 'service',
          'description': 'Credentials used for writing data.'
        }
      },
      'days': {
        'field': {
          'name': 'archive_days',
          'kind': 'integer',
          'order': 1,
          'default': 7
        }
      },
      'storage': {
        'bucket': {
          'field': {
            'name': 'archive_bucket',
            'kind': 'string',
            'order': 2,
            'default': ''
          }
        },
        'path': {
          'field': {
            'name': 'archive_path',
            'kind': 'string',
            'order': 3,
            'default': ''
          }
        }
      },
      'delete': {
        'field': {
          'name': 'archive_delete',
          'kind': 'boolean',
          'order': 4,
          'default': False
        }
      }
    }
  }
]

DAG_FACTORY = DAG_Factory('archive', { 'tasks':TASKS }, INPUTS)
DAG_FACTORY.apply_credentails(USER_CONN_ID, GCP_CONN_ID)
DAG = DAG_FACTORY.execute()

if __name__ == "__main__":
  DAG_FACTORY.print_commandline()
