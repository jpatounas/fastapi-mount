# Copyright (c) 2019, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Provide a custom uvicorn worker that can be configured."""


from starlette.config import Config
from uvicorn.workers import UvicornWorker


config = Config()


class ConfigurableWorker(UvicornWorker):
    """
    Define a UvicornWorker that can be configured by modifying its class attribute.

    All of the command line options for uvicorn are potential configuration options
    (see https://www.uvicorn.org/settings/ for the complete list).

    """

    #: dict: Set the equivalent of uvicorn command line options as keys.
    CONFIG_KWARGS = {
        "root_path": config("SCRIPT_NAME", default=""),
        "proxy_headers": True,
    }
