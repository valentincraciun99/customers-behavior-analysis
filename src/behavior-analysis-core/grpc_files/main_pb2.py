# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: main.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='main.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nmain.proto\"+\n\x0bTestRequest\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\",\n\x0cTestResponse\x12\x0e\n\x06number\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t2h\n\x0bTestService\x12+\n\ntestMethod\x12\x0c.TestRequest\x1a\r.TestResponse\"\x00\x12,\n\x0btestMethod2\x12\x0c.TestRequest\x1a\r.TestResponse\"\x00\x32i\n\x0cTestService2\x12+\n\ntestMethod\x12\x0c.TestRequest\x1a\r.TestResponse\"\x00\x12,\n\x0btestMethod2\x12\x0c.TestRequest\x1a\r.TestResponse\"\x00\x62\x06proto3'
)




_TESTREQUEST = _descriptor.Descriptor(
  name='TestRequest',
  full_name='TestRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='TestRequest.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='TestRequest.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=57,
)


_TESTRESPONSE = _descriptor.Descriptor(
  name='TestResponse',
  full_name='TestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='TestResponse.number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='TestResponse.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=59,
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['TestRequest'] = _TESTREQUEST
DESCRIPTOR.message_types_by_name['TestResponse'] = _TESTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TestRequest = _reflection.GeneratedProtocolMessageType('TestRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTREQUEST,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:TestRequest)
  })
_sym_db.RegisterMessage(TestRequest)

TestResponse = _reflection.GeneratedProtocolMessageType('TestResponse', (_message.Message,), {
  'DESCRIPTOR' : _TESTRESPONSE,
  '__module__' : 'main_pb2'
  # @@protoc_insertion_point(class_scope:TestResponse)
  })
_sym_db.RegisterMessage(TestResponse)



_TESTSERVICE = _descriptor.ServiceDescriptor(
  name='TestService',
  full_name='TestService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=105,
  serialized_end=209,
  methods=[
  _descriptor.MethodDescriptor(
    name='testMethod',
    full_name='TestService.testMethod',
    index=0,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='testMethod2',
    full_name='TestService.testMethod2',
    index=1,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE)

DESCRIPTOR.services_by_name['TestService'] = _TESTSERVICE


_TESTSERVICE2 = _descriptor.ServiceDescriptor(
  name='TestService2',
  full_name='TestService2',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=211,
  serialized_end=316,
  methods=[
  _descriptor.MethodDescriptor(
    name='testMethod',
    full_name='TestService2.testMethod',
    index=0,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='testMethod2',
    full_name='TestService2.testMethod2',
    index=1,
    containing_service=None,
    input_type=_TESTREQUEST,
    output_type=_TESTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TESTSERVICE2)

DESCRIPTOR.services_by_name['TestService2'] = _TESTSERVICE2

# @@protoc_insertion_point(module_scope)
