__METADATA__ = {
    "src_name": 'CADD',
    "src_url": 'http://cadd.gs.washington.edu/',
    "version": '1.2',
    "field": "cadd"
}


def get_mapping():
    mapping = {
        "cadd": {
            "properties": {
                "annotype": {
                    "type": "string",
                    "analyzer": "string_lowercase"
                },
                "chrom": {
                    "type": "string",
                    "analyzer": "string_lowercase"
                },
                "consequence": {
                    "type": "string",
                    "analyzer": "string_lowercase"
                },
                "consscore": {
                    "type": "integer"
                },
                "consdetail": {
                    "type": "string",
                    "analyzer": "string_lowercase"
                },
                "pos": {
                    "type": "long"
                },
                "ref": {
                    "type": "string",
                    "analyzer": "string_lowercase"
                },
                "type": {
                    "type": "string",
                    "analyzer": "string_lowercase"
                },
                "esp": {
                    "properties": {
                        "af": {
                            "type": "float"
                        }
                    }
                },
                "1000g": {
                    "properties": {
                        "af": {
                            "type": "float"
                        }
                    }
                },
                "min_dist_tss": {
                    "type": "integer"
                },
                "min_dist_tse": {
                    "type": "integer"
                },
                "gene": {
                    "properties": {
                        "gene_id": {
                            "type": "string",
                            "analyzer": "string_lowercase"
                        },
                        "genename": {
                            "type": "string",
                            "analyzer": "string_lowercase"
                        }
                    }
                },
                "dst2splice": {
                    "type": "integer"
                },
                "dst2spltype": {
                    "type": "string",
                    "analyzer": "string_lowercase"
                },
                "grantham": {
                    "type": "integer"
                },
                "polyphen": {
                    "properties": {
                        "cat": {
                            "type": "string",
                            "analyzer": "string_lowercase"
                        },
                        "val": {
                            "type": "float"
                        }
                    }
                },
                "sift": {
                    "properties": {
                        "cat": {
                            "type": "string",
                            "analyzer": "string_lowercase"
                        },
                        "val": {
                            "type": "float"
                        }
                    }
                },
                "rawscore": {
                    "type": "float"
                },
                "phred": {
                    "type": "float"
                }
            }
        }
    }
    return mapping
