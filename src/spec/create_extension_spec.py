from pynwb.spec import NWBNamespaceBuilder, NWBGroupSpec
from export_spec import export_spec


def main():
    # the values for ns_builder are auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(doc='An NWB:N extension',
                                     name='ndx-experimenters',
                                     version='0.1.0',
                                     author='Ben Dichter',
                                     contact='ben.dichter@gmail.com')

    # see https://pynwb.readthedocs.io/en/latest/extensions.html#extending-nwb for more information

    nwbfile = NWBGroupSpec(neurodata_type_def='NWBFile_experimenters', neurodata_type_inc='NWBFile',
                           doc='Top level of NWB file.')
    general = nwbfile.add_group(
        name='general',
        doc="Experimental metadata, including protocol, notes and description of hardware"
            "device(s).  COMMENT: The metadata stored in this section should be used to"
            "describe the experiment. Metadata necessary for interpreting the data is stored"
            "with the data. MORE_INFO: General experimental metadata, including animal"
            "strain, experimental protocols, experimenter, devices, etc, are stored under"
            "'general'. Core metadata (e.g., that required to interpret data fields) is"
            "stored with the data itself, and implicitly defined by the file specification"
            "is to use free-form text fields, such as would appear in sentences or paragraphs"
            "from a Methods section. Metadata fields are text to enable them to be more"
            "general, for example to represent ranges instead of numerical values. Machine-readable"
            "metadata is stored as attributes to these free-form datasets. All entries"
            "in the below table are to be included when data is present. Unused groups"
            "(e.g., intracellular_ephys in an optophysiology experiment) should not be"
            "created unless there is data to store within them.")
    general.add_dataset(name='experimenters', shape=(None,), dtype='text', doc='holds multiple experimenters')

    new_data_types = [nwbfile]

    ns_builder.include_type('NWBFile', namespace='core')

    export_spec(ns_builder, new_data_types)


if __name__ == "__main__":
    main()
