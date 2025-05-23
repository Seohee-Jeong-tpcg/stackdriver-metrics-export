#!/usr/bin/env python

# Copyright 2019 Google Inc.
#
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

PUBSUB_VERIFICATION_TOKEN = '9110614f-ce4a-4a80-a2c8-01f681859954'
PUBSUB_TOPIC="metrics_for_bigquery"
BIGQUERY_DATASET='metric_export'
BIGQUERY_TABLE='sd_metrics_export_fin'
BIGQUERY_STATS_TABLE='sd_metrics_stats'
WRITE_BQ_STATS_FLAG=True


GAUGE="GAUGE"
DELTA="DELTA"
CUMULATIVE="CUMULATIVE"

BOOL="BOOL"
INT64="INT64"
DOUBLE="DOUBLE"
STRING="STRING"
DISTRIBUTION="DISTRIBUTION"

ALIGN_DELTA="ALIGN_DELTA"
ALIGN_FRACTION_TRUE="ALIGN_FRACTION_TRUE"
ALIGN_SUM="ALIGN_SUM"
ALIGN_COUNT="ALIGN_COUNT"
ALIGN_NONE="ALIGN_NONE"
REDUCE_FRACTION_TRUE="REDUCE_FRACTION_TRUE"
REDUCE_MEAN="REDUCE_MEAN"
REDUCE_SUM="REDUCE_SUM"
REDUCE_COUNT="REDUCE_COUNT"
REDUCE_NONE="REDUCE_NONE"

bigquery_value_map = {
    "INT64":"int64_value",
    "BOOL":"boolean_value",
    "DOUBLE":"double_value",
    "STRING":"string_value",
    "DISTRIBUTION":"distribution_value"
}

api_value_map = {
    "INT64":"int64Value",
    "BOOL":"booleanValue",
    "DOUBLE":"doubleValue",
    "STRING":"stringValue",
    "DISTRIBUTION":"distributionValue"
}