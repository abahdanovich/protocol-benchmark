# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: helloworld.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncGenerator, List

import betterproto
import grpclib


@dataclass
class HelloRequest(betterproto.Message):
    name: str = betterproto.string_field(1)


@dataclass
class HelloReply(betterproto.Message):
    message: List[str] = betterproto.string_field(1)


@dataclass
class HelloStreamReply(betterproto.Message):
    message: str = betterproto.string_field(1)


@dataclass
class FooBar(betterproto.Message):
    foo: str = betterproto.string_field(1)
    bar: str = betterproto.string_field(2)


@dataclass
class HelloNestedReply(betterproto.Message):
    message: List["FooBar"] = betterproto.message_field(1)


@dataclass
class SomeRequest(betterproto.Message):
    rows_num: int = betterproto.uint32_field(1)


@dataclass
class CustomProps(betterproto.Message):
    foo: str = betterproto.string_field(1)
    bar: int = betterproto.uint32_field(2)


@dataclass
class SomeRecord(betterproto.Message):
    name: str = betterproto.string_field(1)
    address: str = betterproto.string_field(2)
    age: int = betterproto.uint32_field(3)
    country: str = betterproto.string_field(4)
    custom_props: "CustomProps" = betterproto.message_field(5)


@dataclass
class SomeCollection(betterproto.Message):
    rows: List["SomeRecord"] = betterproto.message_field(1)


class GreeterStub(betterproto.ServiceStub):
    async def say_hello(self, *, name: str = "") -> HelloReply:
        request = HelloRequest()
        request.name = name

        return await self._unary_unary(
            "/helloworld.Greeter/SayHello",
            request,
            HelloReply,
        )

    async def say_hello_stream(
        self, *, name: str = ""
    ) -> AsyncGenerator[HelloStreamReply, None]:
        request = HelloRequest()
        request.name = name

        async for response in self._unary_stream(
            "/helloworld.Greeter/SayHelloStream",
            request,
            HelloStreamReply,
        ):
            yield response

    async def say_hello_nested(self, *, name: str = "") -> HelloNestedReply:
        request = HelloRequest()
        request.name = name

        return await self._unary_unary(
            "/helloworld.Greeter/SayHelloNested",
            request,
            HelloNestedReply,
        )

    async def get_some_collection(self, *, rows_num: int = 0) -> SomeCollection:
        request = SomeRequest()
        request.rows_num = rows_num

        return await self._unary_unary(
            "/helloworld.Greeter/GetSomeCollection",
            request,
            SomeCollection,
        )

    async def get_some_stream(
        self, *, rows_num: int = 0
    ) -> AsyncGenerator[SomeRecord, None]:
        request = SomeRequest()
        request.rows_num = rows_num

        async for response in self._unary_stream(
            "/helloworld.Greeter/GetSomeStream",
            request,
            SomeRecord,
        ):
            yield response
