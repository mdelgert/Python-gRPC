# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0csample.proto\x12\rSamplePackage\"F\n\x12\x45ntryCreateRequest\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04\x63ode\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\"a\n\rEntryResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x63ode\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x12\n\ncreated_on\x18\x06 \x01(\x05\x32k\n\rSampleService\x12Z\n\x11\x63reateBulkEntries\x12!.SamplePackage.EntryCreateRequest\x1a\x1c.SamplePackage.EntryResponse\"\x00(\x01\x30\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sample_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENTRYCREATEREQUEST._serialized_start=31
  _ENTRYCREATEREQUEST._serialized_end=101
  _ENTRYRESPONSE._serialized_start=103
  _ENTRYRESPONSE._serialized_end=200
  _SAMPLESERVICE._serialized_start=202
  _SAMPLESERVICE._serialized_end=309
# @@protoc_insertion_point(module_scope)