# Crichton, Admirable Source Configuration Management
# Copyright 2012 British Broadcasting Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#
class pal {
  package { "bbc-pal-barlesque": ensure => "1.8.2-425849.137" }
  package { "bbc-static-barlesque": ensure => "1.8.2-425849.137" }
  package { "bbc-static-barlesque-1.8.2": ensure => "1.8.2-425849.137" }
}
