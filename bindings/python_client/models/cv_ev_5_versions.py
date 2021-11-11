from typing import Any, Dict, List, Type, TypeVar

import attr

from ..models.status_enum import StatusEnum

T = TypeVar("T", bound="CVEv5Versions")


@attr.s(auto_attribs=True)
class CVEv5Versions:
    """CVEv5 Package Version Serializer"""

    version: str
    status: StatusEnum
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        version = self.version
        status = self.status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "version": version,
                "status": status,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        version = d.pop("version")

        status = StatusEnum(d.pop("status"))

        cv_ev_5_versions = cls(
            version=version,
            status=status,
        )

        cv_ev_5_versions.additional_properties = d
        return cv_ev_5_versions

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
