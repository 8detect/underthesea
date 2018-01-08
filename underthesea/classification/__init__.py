# -*- coding: utf-8 -*-
from underthesea.classification.model_fasttext import FastTextPredictor
from underthesea.classification import bank


def classify(X, domain=None):
    """
    Text classification

    Install dependencies and download pretrained model

        $ pip install Cython
        $ pip install future scipy numpy scikit-learn
        $ pip install -U fasttext --no-cache-dir --no-deps --force-reinstall
        $ underthesea data

    Parameters
    ==========

    X: {unicode, str}
        raw sentence
    domain: {None, 'bank'}
        domain of text
            * None: general domain
            * bank: bank domain
    Returns
    =======
    tokens: list
        categories of sentence

    Examples
    --------

    >>> # -*- coding: utf-8 -*-
    >>> from underthesea import classify
    >>> sentence = "HLV ngoại đòi gần tỷ mỗi tháng dẫn dắt tuyển Việt Nam"
    >>> classify(sentence)
    ['The thao']

    >>> sentence = "Tôi rất thích cách phục vụ của nhân viên BIDV"
    >>> classify(sentence, domain='bank')
    ('CUSTOMER SUPPORT',)
    """
    if X == "":
        return None
    if domain == 'bank':
        return bank.classify(X)
    # domain is general
    clf = FastTextPredictor.Instance()
    return clf.predict(X)
