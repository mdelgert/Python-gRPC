# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messages.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0emessages.proto\"!\n\x0eMessageRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"7\n\x0fMessageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x0bmessageType\x18\x02 \x01(\t2=\n\x08Messages\x12\x31\n\nGetMessage\x12\x0f.MessageRequest\x1a\x10.MessageResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'messages_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MESSAGEREQUEST._serialized_start=18
  _MESSAGEREQUEST._serialized_end=51
  _MESSAGERESPONSE._serialized_start=53
  _MESSAGERESPONSE._serialized_end=108
  _MESSAGES._serialized_start=110
  _MESSAGES._serialized_end=171
# @@protoc_insertion_point(module_scope)