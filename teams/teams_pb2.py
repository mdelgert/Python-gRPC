# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: teams.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bteams.proto\"\x1b\n\x0bTeamRequest\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\".\n\x0cTeamResponse\x12\x0c\n\x04\x63ity\x18\x01 \x01(\t\x12\x10\n\x08nickname\x18\x02 \x01(\t21\n\x05Teams\x12(\n\x07GetTeam\x12\x0c.TeamRequest\x1a\r.TeamResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'teams_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TEAMREQUEST._serialized_start=15
  _TEAMREQUEST._serialized_end=42
  _TEAMRESPONSE._serialized_start=44
  _TEAMRESPONSE._serialized_end=90
  _TEAMS._serialized_start=92
  _TEAMS._serialized_end=141
# @@protoc_insertion_point(module_scope)
