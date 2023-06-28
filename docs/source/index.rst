.. Projeto Teste documentation master file, created by
   sphinx-quickstart on Fri Jun 23 16:23:21 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Projeto Teste's documentation!
=========================================

Welcome to the Sphinx Guide I'm creating as a source of study of the tool

.. image:: /images/gato.jpg

- Test 1
- **Test 2**
- *Test 3*

Entrar no :ref:`Arquivo Teste<settingup>` por meio de um link

.. toctree::
   :maxdepth: 2
   :caption: Label to the Contents:

   arquivoteste

.. toctree::
   :maxdepth: 2
   :caption: Other Contents:

   arquivoteste2

.. toctree::
   :maxdepth: 5
   :caption: Arquivos Python:

   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

