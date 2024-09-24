


class FilterModule(object):
    def filters(self):
        return {
            'xml2json': xml2json,
            'ftr_zone': ftr_zone,
            'validate_zone': validate_zone,
            'ftr_addrobj': ftr_addrobj,
            'validate_addrobj': validate_addrobj,
            'ftr_servobj': ftr_servobj,
            'validate_servobj': validate_servobj
        }
