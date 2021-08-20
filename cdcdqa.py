from cdqa.utils.download import download_squad, download_model, download_bnpp_data

from cdqa.utils.download import download_squad, download_model, download_bnpp_data

directory = './data'

# Downloading data
download_squad(dir=directory)
download_bnpp_data(dir=directory)

# Downloading pre-trained BERT fine-tuned on SQuAD 1.1
download_model('bert-squad_1.1', dir=directory)

# Downloading pre-trained DistilBERT fine-tuned on SQuAD 1.1
download_model('distilbert-squad_1.1', dir=directory)