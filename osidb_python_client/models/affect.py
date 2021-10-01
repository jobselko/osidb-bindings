from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.affect_state_enum import AffectStateEnum
from ..models.affect_type_enum import AffectTypeEnum
from ..models.blank_enum import BlankEnum
from ..models.impact_enum import ImpactEnum
from ..models.null_enum import NullEnum
from ..models.resolution_enum import ResolutionEnum
from ..models.tracker import Tracker
from ..types import UNSET, Unset

T = TypeVar("T", bound="Affect")


@attr.s(auto_attribs=True)
class Affect:
    """Affect serializer"""

    uuid: str
    trackers: List[Tracker]
    type: Union[AffectTypeEnum, BlankEnum, None, NullEnum, Unset] = UNSET
    state: Union[AffectStateEnum, BlankEnum, None, NullEnum, Unset] = UNSET
    resolution: Union[BlankEnum, None, NullEnum, ResolutionEnum, Unset] = UNSET
    ps_module: Union[Unset, None, str] = UNSET
    ps_component: Union[Unset, None, str] = UNSET
    module_name: Union[Unset, None, str] = UNSET
    module_stream: Union[Unset, None, str] = UNSET
    component: Union[Unset, None, str] = UNSET
    statement: Union[Unset, None, str] = UNSET
    impact: Union[BlankEnum, ImpactEnum, None, NullEnum, Unset] = UNSET
    cvss2: Union[Unset, None, str] = UNSET
    cvss2_score: Union[Unset, None, float] = UNSET
    cvss3: Union[Unset, None, str] = UNSET
    cvss3_score: Union[Unset, None, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        uuid = self.uuid
        trackers = []
        for trackers_item_data in self.trackers:
            trackers_item = trackers_item_data.to_dict()

            trackers.append(trackers_item)

        type: Union[None, NoneType, Unset, str]
        if isinstance(self.type, Unset):
            type = UNSET
        elif self.type is None:
            type = None
        elif isinstance(self.type, AffectTypeEnum):
            type = UNSET
            if not isinstance(self.type, Unset):
                type = self.type.value

        elif isinstance(self.type, BlankEnum):
            type = UNSET
            if not isinstance(self.type, Unset):
                type = self.type.value

        else:
            type = UNSET
            if not isinstance(self.type, Unset):
                type = self.type.value

        state: Union[None, NoneType, Unset, str]
        if isinstance(self.state, Unset):
            state = UNSET
        elif self.state is None:
            state = None
        elif isinstance(self.state, AffectStateEnum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        elif isinstance(self.state, BlankEnum):
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        else:
            state = UNSET
            if not isinstance(self.state, Unset):
                state = self.state.value

        resolution: Union[None, NoneType, Unset, str]
        if isinstance(self.resolution, Unset):
            resolution = UNSET
        elif self.resolution is None:
            resolution = None
        elif isinstance(self.resolution, ResolutionEnum):
            resolution = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = self.resolution.value

        elif isinstance(self.resolution, BlankEnum):
            resolution = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = self.resolution.value

        else:
            resolution = UNSET
            if not isinstance(self.resolution, Unset):
                resolution = self.resolution.value

        ps_module = self.ps_module
        ps_component = self.ps_component
        module_name = self.module_name
        module_stream = self.module_stream
        component = self.component
        statement = self.statement
        impact: Union[None, NoneType, Unset, str]
        if isinstance(self.impact, Unset):
            impact = UNSET
        elif self.impact is None:
            impact = None
        elif isinstance(self.impact, ImpactEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):
                impact = self.impact.value

        elif isinstance(self.impact, BlankEnum):
            impact = UNSET
            if not isinstance(self.impact, Unset):
                impact = self.impact.value

        else:
            impact = UNSET
            if not isinstance(self.impact, Unset):
                impact = self.impact.value

        cvss2 = self.cvss2
        cvss2_score = self.cvss2_score
        cvss3 = self.cvss3
        cvss3_score = self.cvss3_score

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
                "trackers": trackers,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type
        if state is not UNSET:
            field_dict["state"] = state
        if resolution is not UNSET:
            field_dict["resolution"] = resolution
        if ps_module is not UNSET:
            field_dict["ps_module"] = ps_module
        if ps_component is not UNSET:
            field_dict["ps_component"] = ps_component
        if module_name is not UNSET:
            field_dict["module_name"] = module_name
        if module_stream is not UNSET:
            field_dict["module_stream"] = module_stream
        if component is not UNSET:
            field_dict["component"] = component
        if statement is not UNSET:
            field_dict["statement"] = statement
        if impact is not UNSET:
            field_dict["impact"] = impact
        if cvss2 is not UNSET:
            field_dict["cvss2"] = cvss2
        if cvss2_score is not UNSET:
            field_dict["cvss2_score"] = cvss2_score
        if cvss3 is not UNSET:
            field_dict["cvss3"] = cvss3
        if cvss3_score is not UNSET:
            field_dict["cvss3_score"] = cvss3_score

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        uuid = d.pop("uuid")

        trackers = []
        _trackers = d.pop("trackers")
        for trackers_item_data in _trackers:
            trackers_item = Tracker.from_dict(trackers_item_data)

            trackers.append(trackers_item)

        def _parse_type(data: object) -> Union[AffectTypeEnum, BlankEnum, None, NullEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _type_type_0 = data
                type_type_0: Union[Unset, AffectTypeEnum]
                if isinstance(_type_type_0, Unset):
                    type_type_0 = UNSET
                else:
                    type_type_0 = AffectTypeEnum(_type_type_0)

                return type_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _type_type_1 = data
                type_type_1: Union[Unset, BlankEnum]
                if isinstance(_type_type_1, Unset):
                    type_type_1 = UNSET
                else:
                    type_type_1 = BlankEnum(_type_type_1)

                return type_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, NoneType):
                raise TypeError()
            _type_type_2 = data
            type_type_2: Union[Unset, NullEnum]
            if isinstance(_type_type_2, Unset):
                type_type_2 = UNSET
            else:
                type_type_2 = NullEnum(_type_type_2)

            return type_type_2

        type = _parse_type(d.pop("type", UNSET))

        def _parse_state(data: object) -> Union[AffectStateEnum, BlankEnum, None, NullEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _state_type_0 = data
                state_type_0: Union[Unset, AffectStateEnum]
                if isinstance(_state_type_0, Unset):
                    state_type_0 = UNSET
                else:
                    state_type_0 = AffectStateEnum(_state_type_0)

                return state_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _state_type_1 = data
                state_type_1: Union[Unset, BlankEnum]
                if isinstance(_state_type_1, Unset):
                    state_type_1 = UNSET
                else:
                    state_type_1 = BlankEnum(_state_type_1)

                return state_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, NoneType):
                raise TypeError()
            _state_type_2 = data
            state_type_2: Union[Unset, NullEnum]
            if isinstance(_state_type_2, Unset):
                state_type_2 = UNSET
            else:
                state_type_2 = NullEnum(_state_type_2)

            return state_type_2

        state = _parse_state(d.pop("state", UNSET))

        def _parse_resolution(data: object) -> Union[BlankEnum, None, NullEnum, ResolutionEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _resolution_type_0 = data
                resolution_type_0: Union[Unset, ResolutionEnum]
                if isinstance(_resolution_type_0, Unset):
                    resolution_type_0 = UNSET
                else:
                    resolution_type_0 = ResolutionEnum(_resolution_type_0)

                return resolution_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _resolution_type_1 = data
                resolution_type_1: Union[Unset, BlankEnum]
                if isinstance(_resolution_type_1, Unset):
                    resolution_type_1 = UNSET
                else:
                    resolution_type_1 = BlankEnum(_resolution_type_1)

                return resolution_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, NoneType):
                raise TypeError()
            _resolution_type_2 = data
            resolution_type_2: Union[Unset, NullEnum]
            if isinstance(_resolution_type_2, Unset):
                resolution_type_2 = UNSET
            else:
                resolution_type_2 = NullEnum(_resolution_type_2)

            return resolution_type_2

        resolution = _parse_resolution(d.pop("resolution", UNSET))

        ps_module = d.pop("ps_module", UNSET)

        ps_component = d.pop("ps_component", UNSET)

        module_name = d.pop("module_name", UNSET)

        module_stream = d.pop("module_stream", UNSET)

        component = d.pop("component", UNSET)

        statement = d.pop("statement", UNSET)

        def _parse_impact(data: object) -> Union[BlankEnum, ImpactEnum, None, NullEnum, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _impact_type_0 = data
                impact_type_0: Union[Unset, ImpactEnum]
                if isinstance(_impact_type_0, Unset):
                    impact_type_0 = UNSET
                else:
                    impact_type_0 = ImpactEnum(_impact_type_0)

                return impact_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                _impact_type_1 = data
                impact_type_1: Union[Unset, BlankEnum]
                if isinstance(_impact_type_1, Unset):
                    impact_type_1 = UNSET
                else:
                    impact_type_1 = BlankEnum(_impact_type_1)

                return impact_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, NoneType):
                raise TypeError()
            _impact_type_2 = data
            impact_type_2: Union[Unset, NullEnum]
            if isinstance(_impact_type_2, Unset):
                impact_type_2 = UNSET
            else:
                impact_type_2 = NullEnum(_impact_type_2)

            return impact_type_2

        impact = _parse_impact(d.pop("impact", UNSET))

        cvss2 = d.pop("cvss2", UNSET)

        cvss2_score = d.pop("cvss2_score", UNSET)

        cvss3 = d.pop("cvss3", UNSET)

        cvss3_score = d.pop("cvss3_score", UNSET)

        affect = cls(
            uuid=uuid,
            trackers=trackers,
            type=type,
            state=state,
            resolution=resolution,
            ps_module=ps_module,
            ps_component=ps_component,
            module_name=module_name,
            module_stream=module_stream,
            component=component,
            statement=statement,
            impact=impact,
            cvss2=cvss2,
            cvss2_score=cvss2_score,
            cvss3=cvss3,
            cvss3_score=cvss3_score,
        )

        affect.additional_properties = d
        return affect

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
