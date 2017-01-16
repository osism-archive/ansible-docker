#!/usr/bin/env bash
set -x

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Available environment variables:
#
# NEXUS_ARTIFACT_REPOSITORY
# NEXUS_ARTIFACT_NAME
# NEXUS_ARTIFACT_TAG
# NEXUS_USERNAME
# NEXUS_PASSWORD
# NEXUS_SERVER

# Set default values:

ARCHIVE=$NEXUS_ARTIFACT_NAME-$NEXUS_ARTIFACT_TAG.tar.gz

tar cvzf $ARCHIVE README.md defaults files handlers meta tasks templates
mkdir $NEXUS_ARTIFACT_NAME
tar xvzf $ARCHIVE -C $NEXUS_ARTIFACT_NAME
tar cvzf $ARCHIVE $NEXUS_ARTIFACT_NAME
curl -v --user "$NEXUS_USERNAME:$NEXUS_PASSWORD" --upload-file $ARCHIVE https://$NEXUS_SERVER/repository/$NEXUS_ARTIFACT_REPOSITORY/$ARCHIVE
rm -f $ARCHIVE
rm -rf $NEXUS_ARTIFACT_NAME
