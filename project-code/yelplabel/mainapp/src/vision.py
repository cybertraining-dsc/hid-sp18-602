# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64
import json
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials

API_KEY='AIzaSyDASvlgiXOKlf9Spr183d-ITKkWi844nII'
DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'


class VisionApi(object):
    def __init__(self):
        self.vision = self._create_client()


    def _create_client(self):
        #credentials = GoogleCredentials.get_application_default()
        return discovery.build(
            'vision', 'v1', developerKey=API_KEY,
            discoveryServiceUrl=DISCOVERY_URL)



    def detect_labels(self, images,max_results=1,num_retries=3):
        """Uses the Vision API to annotate  image  """
        request = self.vision.images().annotate(
        body={'requests': [{
                             'image': {
                                 #'content': str(base64.b64encode(images).decode('UTF-8'))
                                 'source':{
                                    'imageUri':images
                                     }
               		 },
                	'features': [{
                    		 'type': 'LABEL_DETECTION',
                   		 'maxResults': max_results,
               		 }]
        	    }]
        	})
        #request=self.vision.images().annotate(body)
        
        #print(body)
        response = request.execute(num_retries=num_retries)
	label=response['responses'][0]['labelAnnotations'][0]['description']

        return label
