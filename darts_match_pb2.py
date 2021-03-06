# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: darts_match.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='darts_match.proto',
  package='app',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x64\x61rts_match.proto\x12\x03\x61pp\"3\n\x0cMatchRequest\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x11\n\tmatchType\x18\x02 \x01(\t\" \n\rMatchResponce\x12\x0f\n\x07matchId\x18\x01 \x01(\x0c\"4\n\x0fRegisterRequest\x12\x0f\n\x07matchId\x18\x01 \x01(\x0c\x12\x10\n\x08userName\x18\x02 \x01(\t\"\'\n\x10RegisterResponce\x12\x13\n\x0bplayerIndex\x18\x01 \x01(\x05\"\"\n\x0f\x46inalizeRequest\x12\x0f\n\x07matchId\x18\x01 \x01(\x0c\"\x12\n\x10\x46inalizeResponce\"\x87\x01\n\x04\x44\x61rt\x12-\n\nmultiplier\x18\x01 \x01(\x0e\x32\x19.app.Dart.DartsMultiplier\x12\x0f\n\x07segment\x18\x02 \x01(\x05\"?\n\x0f\x44\x61rtsMultiplier\x12\x08\n\x04MISS\x10\x00\x12\n\n\x06SINGLE\x10\x01\x12\n\n\x06\x44OUBLE\x10\x02\x12\n\n\x06TREBLE\x10\x03\"N\n\x0cVisitRequest\x12\x0f\n\x07matchId\x18\x01 \x01(\x0c\x12\x13\n\x0bplayerIndex\x18\x02 \x01(\x05\x12\x18\n\x05visit\x18\x03 \x03(\x0b\x32\t.app.Dart\"0\n\rVisitResponce\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"M\n\x0bListRequest\x12\x0f\n\x07matchId\x18\x01 \x01(\x0c\x12\x13\n\x0bplayerIndex\x18\x02 \x01(\x05\x12\x18\n\x05visit\x18\x03 \x03(\x0b\x32\t.app.Dart\"/\n\x06Player\x12\x10\n\x08userName\x18\x01 \x01(\t\x12\x13\n\x0bplayerIndex\x18\x02 \x01(\x05\"%\n\x05Match\x12\x1c\n\x07players\x18\x01 \x03(\x0b\x32\x0b.app.Player\"+\n\x0cListResponce\x12\x1b\n\x07matches\x18\x01 \x03(\x0b\x32\n.app.Match\"\x0e\n\x0cWatchRequest\"U\n\rWatchResponce\x12\x1b\n\x06player\x18\x01 \x01(\x0b\x32\x0b.app.Player\x12\x18\n\x05\x64\x61rts\x18\x02 \x03(\x0b\x32\t.app.Dart\x12\r\n\x05score\x18\x03 \x01(\x05\x32\xed\x02\n\nDartsMatch\x12\x36\n\x0b\x43reateMatch\x12\x11.app.MatchRequest\x1a\x12.app.MatchResponce\"\x00\x12?\n\x0eRegisterPlayer\x12\x14.app.RegisterRequest\x1a\x15.app.RegisterResponce\"\x00\x12>\n\rFinalizeMatch\x12\x14.app.FinalizeRequest\x1a\x15.app.FinalizeResponce\"\x00\x12\x37\n\x0cProcessVisit\x12\x11.app.VisitRequest\x1a\x12.app.VisitResponce\"\x00\x12\x34\n\x0bListMatches\x12\x10.app.ListRequest\x1a\x11.app.ListResponce\"\x00\x12\x37\n\nWatchMatch\x12\x11.app.WatchRequest\x1a\x12.app.WatchResponce\"\x00\x30\x01\x62\x06proto3'
)



_DART_DARTSMULTIPLIER = _descriptor.EnumDescriptor(
  name='DartsMultiplier',
  full_name='app.Dart.DartsMultiplier',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MISS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SINGLE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DOUBLE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TREBLE', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=337,
  serialized_end=400,
)
_sym_db.RegisterEnumDescriptor(_DART_DARTSMULTIPLIER)


_MATCHREQUEST = _descriptor.Descriptor(
  name='MatchRequest',
  full_name='app.MatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='app.MatchRequest.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='matchType', full_name='app.MatchRequest.matchType', index=1,
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
  serialized_start=26,
  serialized_end=77,
)


_MATCHRESPONCE = _descriptor.Descriptor(
  name='MatchResponce',
  full_name='app.MatchResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matchId', full_name='app.MatchResponce.matchId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=79,
  serialized_end=111,
)


_REGISTERREQUEST = _descriptor.Descriptor(
  name='RegisterRequest',
  full_name='app.RegisterRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matchId', full_name='app.RegisterRequest.matchId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userName', full_name='app.RegisterRequest.userName', index=1,
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
  serialized_start=113,
  serialized_end=165,
)


_REGISTERRESPONCE = _descriptor.Descriptor(
  name='RegisterResponce',
  full_name='app.RegisterResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='playerIndex', full_name='app.RegisterResponce.playerIndex', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=167,
  serialized_end=206,
)


_FINALIZEREQUEST = _descriptor.Descriptor(
  name='FinalizeRequest',
  full_name='app.FinalizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matchId', full_name='app.FinalizeRequest.matchId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=208,
  serialized_end=242,
)


_FINALIZERESPONCE = _descriptor.Descriptor(
  name='FinalizeResponce',
  full_name='app.FinalizeResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=244,
  serialized_end=262,
)


_DART = _descriptor.Descriptor(
  name='Dart',
  full_name='app.Dart',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='multiplier', full_name='app.Dart.multiplier', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='segment', full_name='app.Dart.segment', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DART_DARTSMULTIPLIER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=400,
)


_VISITREQUEST = _descriptor.Descriptor(
  name='VisitRequest',
  full_name='app.VisitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matchId', full_name='app.VisitRequest.matchId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playerIndex', full_name='app.VisitRequest.playerIndex', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visit', full_name='app.VisitRequest.visit', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=402,
  serialized_end=480,
)


_VISITRESPONCE = _descriptor.Descriptor(
  name='VisitResponce',
  full_name='app.VisitResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='app.VisitResponce.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='app.VisitResponce.message', index=1,
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
  serialized_start=482,
  serialized_end=530,
)


_LISTREQUEST = _descriptor.Descriptor(
  name='ListRequest',
  full_name='app.ListRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matchId', full_name='app.ListRequest.matchId', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playerIndex', full_name='app.ListRequest.playerIndex', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visit', full_name='app.ListRequest.visit', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=532,
  serialized_end=609,
)


_PLAYER = _descriptor.Descriptor(
  name='Player',
  full_name='app.Player',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='userName', full_name='app.Player.userName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='playerIndex', full_name='app.Player.playerIndex', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=611,
  serialized_end=658,
)


_MATCH = _descriptor.Descriptor(
  name='Match',
  full_name='app.Match',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='players', full_name='app.Match.players', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=660,
  serialized_end=697,
)


_LISTRESPONCE = _descriptor.Descriptor(
  name='ListResponce',
  full_name='app.ListResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='matches', full_name='app.ListResponce.matches', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=699,
  serialized_end=742,
)


_WATCHREQUEST = _descriptor.Descriptor(
  name='WatchRequest',
  full_name='app.WatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
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
  serialized_start=744,
  serialized_end=758,
)


_WATCHRESPONCE = _descriptor.Descriptor(
  name='WatchResponce',
  full_name='app.WatchResponce',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='player', full_name='app.WatchResponce.player', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='darts', full_name='app.WatchResponce.darts', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='score', full_name='app.WatchResponce.score', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=760,
  serialized_end=845,
)

_DART.fields_by_name['multiplier'].enum_type = _DART_DARTSMULTIPLIER
_DART_DARTSMULTIPLIER.containing_type = _DART
_VISITREQUEST.fields_by_name['visit'].message_type = _DART
_LISTREQUEST.fields_by_name['visit'].message_type = _DART
_MATCH.fields_by_name['players'].message_type = _PLAYER
_LISTRESPONCE.fields_by_name['matches'].message_type = _MATCH
_WATCHRESPONCE.fields_by_name['player'].message_type = _PLAYER
_WATCHRESPONCE.fields_by_name['darts'].message_type = _DART
DESCRIPTOR.message_types_by_name['MatchRequest'] = _MATCHREQUEST
DESCRIPTOR.message_types_by_name['MatchResponce'] = _MATCHRESPONCE
DESCRIPTOR.message_types_by_name['RegisterRequest'] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name['RegisterResponce'] = _REGISTERRESPONCE
DESCRIPTOR.message_types_by_name['FinalizeRequest'] = _FINALIZEREQUEST
DESCRIPTOR.message_types_by_name['FinalizeResponce'] = _FINALIZERESPONCE
DESCRIPTOR.message_types_by_name['Dart'] = _DART
DESCRIPTOR.message_types_by_name['VisitRequest'] = _VISITREQUEST
DESCRIPTOR.message_types_by_name['VisitResponce'] = _VISITRESPONCE
DESCRIPTOR.message_types_by_name['ListRequest'] = _LISTREQUEST
DESCRIPTOR.message_types_by_name['Player'] = _PLAYER
DESCRIPTOR.message_types_by_name['Match'] = _MATCH
DESCRIPTOR.message_types_by_name['ListResponce'] = _LISTRESPONCE
DESCRIPTOR.message_types_by_name['WatchRequest'] = _WATCHREQUEST
DESCRIPTOR.message_types_by_name['WatchResponce'] = _WATCHRESPONCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MatchRequest = _reflection.GeneratedProtocolMessageType('MatchRequest', (_message.Message,), {
  'DESCRIPTOR' : _MATCHREQUEST,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.MatchRequest)
  })
_sym_db.RegisterMessage(MatchRequest)

MatchResponce = _reflection.GeneratedProtocolMessageType('MatchResponce', (_message.Message,), {
  'DESCRIPTOR' : _MATCHRESPONCE,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.MatchResponce)
  })
_sym_db.RegisterMessage(MatchResponce)

RegisterRequest = _reflection.GeneratedProtocolMessageType('RegisterRequest', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERREQUEST,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.RegisterRequest)
  })
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponce = _reflection.GeneratedProtocolMessageType('RegisterResponce', (_message.Message,), {
  'DESCRIPTOR' : _REGISTERRESPONCE,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.RegisterResponce)
  })
_sym_db.RegisterMessage(RegisterResponce)

FinalizeRequest = _reflection.GeneratedProtocolMessageType('FinalizeRequest', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZEREQUEST,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.FinalizeRequest)
  })
_sym_db.RegisterMessage(FinalizeRequest)

FinalizeResponce = _reflection.GeneratedProtocolMessageType('FinalizeResponce', (_message.Message,), {
  'DESCRIPTOR' : _FINALIZERESPONCE,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.FinalizeResponce)
  })
_sym_db.RegisterMessage(FinalizeResponce)

Dart = _reflection.GeneratedProtocolMessageType('Dart', (_message.Message,), {
  'DESCRIPTOR' : _DART,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.Dart)
  })
_sym_db.RegisterMessage(Dart)

VisitRequest = _reflection.GeneratedProtocolMessageType('VisitRequest', (_message.Message,), {
  'DESCRIPTOR' : _VISITREQUEST,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.VisitRequest)
  })
_sym_db.RegisterMessage(VisitRequest)

VisitResponce = _reflection.GeneratedProtocolMessageType('VisitResponce', (_message.Message,), {
  'DESCRIPTOR' : _VISITRESPONCE,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.VisitResponce)
  })
_sym_db.RegisterMessage(VisitResponce)

ListRequest = _reflection.GeneratedProtocolMessageType('ListRequest', (_message.Message,), {
  'DESCRIPTOR' : _LISTREQUEST,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.ListRequest)
  })
_sym_db.RegisterMessage(ListRequest)

Player = _reflection.GeneratedProtocolMessageType('Player', (_message.Message,), {
  'DESCRIPTOR' : _PLAYER,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.Player)
  })
_sym_db.RegisterMessage(Player)

Match = _reflection.GeneratedProtocolMessageType('Match', (_message.Message,), {
  'DESCRIPTOR' : _MATCH,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.Match)
  })
_sym_db.RegisterMessage(Match)

ListResponce = _reflection.GeneratedProtocolMessageType('ListResponce', (_message.Message,), {
  'DESCRIPTOR' : _LISTRESPONCE,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.ListResponce)
  })
_sym_db.RegisterMessage(ListResponce)

WatchRequest = _reflection.GeneratedProtocolMessageType('WatchRequest', (_message.Message,), {
  'DESCRIPTOR' : _WATCHREQUEST,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.WatchRequest)
  })
_sym_db.RegisterMessage(WatchRequest)

WatchResponce = _reflection.GeneratedProtocolMessageType('WatchResponce', (_message.Message,), {
  'DESCRIPTOR' : _WATCHRESPONCE,
  '__module__' : 'darts_match_pb2'
  # @@protoc_insertion_point(class_scope:app.WatchResponce)
  })
_sym_db.RegisterMessage(WatchResponce)



_DARTSMATCH = _descriptor.ServiceDescriptor(
  name='DartsMatch',
  full_name='app.DartsMatch',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=848,
  serialized_end=1213,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateMatch',
    full_name='app.DartsMatch.CreateMatch',
    index=0,
    containing_service=None,
    input_type=_MATCHREQUEST,
    output_type=_MATCHRESPONCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterPlayer',
    full_name='app.DartsMatch.RegisterPlayer',
    index=1,
    containing_service=None,
    input_type=_REGISTERREQUEST,
    output_type=_REGISTERRESPONCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='FinalizeMatch',
    full_name='app.DartsMatch.FinalizeMatch',
    index=2,
    containing_service=None,
    input_type=_FINALIZEREQUEST,
    output_type=_FINALIZERESPONCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ProcessVisit',
    full_name='app.DartsMatch.ProcessVisit',
    index=3,
    containing_service=None,
    input_type=_VISITREQUEST,
    output_type=_VISITRESPONCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ListMatches',
    full_name='app.DartsMatch.ListMatches',
    index=4,
    containing_service=None,
    input_type=_LISTREQUEST,
    output_type=_LISTRESPONCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='WatchMatch',
    full_name='app.DartsMatch.WatchMatch',
    index=5,
    containing_service=None,
    input_type=_WATCHREQUEST,
    output_type=_WATCHRESPONCE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_DARTSMATCH)

DESCRIPTOR.services_by_name['DartsMatch'] = _DARTSMATCH

# @@protoc_insertion_point(module_scope)
