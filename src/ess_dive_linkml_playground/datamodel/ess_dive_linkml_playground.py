# Auto generated from ess_dive_linkml_playground.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-12-19T20:44:46
# Schema: ess-dive-linkml-playground
#
# id: https://w3id.org/ess-dive-linkml-playground
# description: This is a collaborative repo for exploring schema creation and data validation for ESS-DIVE, using
#              LinkML
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PLAYGROUND = CurieNamespace('playground', 'https://example.com/ess-dive-linkml-playground')
DEFAULT_ = PLAYGROUND


# Types

# Class references
class ObservationBasin3dId(extended_str):
    pass


@dataclass
class Observation(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLAYGROUND.Observation
    class_class_curie: ClassVar[str] = "playground:Observation"
    class_name: ClassVar[str] = "Observation"
    class_model_uri: ClassVar[URIRef] = PLAYGROUND.Observation

    basin3d_id: Union[str, ObservationBasin3dId] = None
    description: Optional[str] = None
    categories: Optional[str] = None
    units: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.basin3d_id):
            self.MissingRequiredField("basin3d_id")
        if not isinstance(self.basin3d_id, ObservationBasin3dId):
            self.basin3d_id = ObservationBasin3dId(self.basin3d_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.categories is not None and not isinstance(self.categories, str):
            self.categories = str(self.categories)

        if self.units is not None and not isinstance(self.units, str):
            self.units = str(self.units)

        super().__post_init__(**kwargs)


@dataclass
class Container(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = PLAYGROUND.Container
    class_class_curie: ClassVar[str] = "playground:Container"
    class_name: ClassVar[str] = "Container"
    class_model_uri: ClassVar[URIRef] = PLAYGROUND.Container

    observation_list: Optional[Union[Dict[Union[str, ObservationBasin3dId], Union[dict, Observation]], List[Union[dict, Observation]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(slot_name="observation_list", slot_type=Observation, key_name="basin3d_id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.basin3d_id = Slot(uri=PLAYGROUND.basin3d_id, name="basin3d_id", curie=PLAYGROUND.curie('basin3d_id'),
                   model_uri=PLAYGROUND.basin3d_id, domain=None, range=URIRef)

slots.description = Slot(uri=PLAYGROUND.description, name="description", curie=PLAYGROUND.curie('description'),
                   model_uri=PLAYGROUND.description, domain=None, range=Optional[str])

slots.categories = Slot(uri=PLAYGROUND.categories, name="categories", curie=PLAYGROUND.curie('categories'),
                   model_uri=PLAYGROUND.categories, domain=None, range=Optional[str])

slots.units = Slot(uri=PLAYGROUND.units, name="units", curie=PLAYGROUND.curie('units'),
                   model_uri=PLAYGROUND.units, domain=None, range=Optional[str])

slots.container__observation_list = Slot(uri=PLAYGROUND.observation_list, name="container__observation_list", curie=PLAYGROUND.curie('observation_list'),
                   model_uri=PLAYGROUND.container__observation_list, domain=None, range=Optional[Union[Dict[Union[str, ObservationBasin3dId], Union[dict, Observation]], List[Union[dict, Observation]]]])