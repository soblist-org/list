from datetime import datetime
from typing import List

from pydantic import BaseModel, Field


class EventMeta(BaseModel):
    """
    Model for event meta.
    """

    date: datetime = Field(..., title="datetime", description="event datetime")
    addr: str = Field(..., title="address", description="event address")
    archive_url: str = Field(..., title="archive url")
    ref_urls: List[str] = Field(..., title="reference urls")


class Activity(BaseModel):
    """
    Model for activity.
    """

    pass


class Case(BaseModel):
    """
    Model for case.
    """

    meta: EventMeta = Field(..., title="case meta information")
    title: str = Field(..., title="case title")
    content: str = Field(..., title="case detail content")
    images: List[str] = Field(..., title="images urls")


class SunOfBitch(BaseModel):
    """
    Model for son of bitch.
    """

    name: str = Field(..., title="name", description="original name")
    en_name: str = Field(title="english name", description="ascii name")
    addr: str = Field(title="address", description="address")
    school_name: str = Field(
        title="school name", description="school | university | college name"
    )
    id_number: str = Field(
        title="citizen ID number", description="citizen identifier number"
    )
    pic_src: str = Field(
        title="picture URL source", description="picture URL source"
    )
    birth: str = Field(title="birth date", description="birth date in general")
    cases: List[Case] = Field(..., title="sob related cases")
    latest_activities: List[Activity] = Field(
        title="sob latest activities, update frequently"
    )
