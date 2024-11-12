Sphinx Image with Language
==========================

Here there are two examples of use of the ``image`` directive. One with the file extension (``.png``) and the other with a wildcard asterisk (``.*``).

With extension
##############

The image here has the URI ``img/balloon.png``, but the actual file is called ``img/balloon.en.png``:

.. code-block:: reStructuredText

   .. image:: img/balloon.png
      :alt: A balloon icon
      :align: right
      :width: 200

.. image:: img/balloon.png
   :alt: A balloon icon
   :align: right
   :width: 200

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus pretium blandit tortor vitae efficitur. Vestibulum eget venenatis eros. Cras euismod eget justo id sodales. Vestibulum a ullamcorper turpis. Suspendisse potenti. Curabitur ac condimentum dui.

Donec mollis leo lorem, vel dictum nisi efficitur id. Praesent mollis vel ante efficitur placerat. Nunc nec eros ac ex laoreet tristique non ac neque. Cras felis elit, eleifend eget nisl aliquet, maximus maximus justo.

With an asterisk
################

The image here has the URI ``img/balloon.*``, but the actual file is called ``img/balloon.en.png``:

.. code-block:: reStructuredText

   .. image:: img/balloon.*
      :alt: A balloon icon
      :align: right
      :width: 200

.. image:: img/balloon.*
   :alt: A balloon icon
   :align: right
   :width: 200

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus pretium blandit tortor vitae efficitur. Vestibulum eget venenatis eros. Cras euismod eget justo id sodales. Vestibulum a ullamcorper turpis. Suspendisse potenti. Curabitur ac condimentum dui.

Donec mollis leo lorem, vel dictum nisi efficitur id. Praesent mollis vel ante efficitur placerat. Nunc nec eros ac ex laoreet tristique non ac neque. Cras felis elit, eleifend eget nisl aliquet, maximus maximus justo.
