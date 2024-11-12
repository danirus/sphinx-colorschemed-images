CS Image with Language
======================

Here there are two examples of use of the ``cs_image`` directive. One with the file extension (``.png``) and the other with an asterisk (``.*``).

The image paths inferred in both cases are:

* ``img/balloon.en.dark.png``, and
* ``img/balloon.en.light.png``


With extension
##############

The image here has the URI ``img/balloon.png``. The code:

.. code-block:: reStructuredText

   .. cs_image:: img/balloon.png
      :alt: A balloon icon
      :align: right
      :width: 200

.. cs_image:: img/balloon.png
   :alt: A balloon icon
   :align: right
   :width: 200

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus pretium blandit tortor vitae efficitur. Vestibulum eget venenatis eros. Cras euismod eget justo id sodales. Vestibulum a ullamcorper turpis. Suspendisse potenti. Curabitur ac condimentum dui.

Donec mollis leo lorem, vel dictum nisi efficitur id. Praesent mollis vel ante efficitur placerat. Nunc nec eros ac ex laoreet tristique non ac neque. Cras felis elit, eleifend eget nisl aliquet, maximus maximus justo.

With an asterisk
################

The image here has the URI ``img/balloon.*``. The code:

.. code-block:: reStructuredText

   .. cs_image:: img/balloon.*
      :alt: A balloon icon
      :align: right
      :width: 200

.. cs_image:: img/balloon.*
   :alt: A balloon icon
   :align: right
   :width: 200

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus pretium blandit tortor vitae efficitur. Vestibulum eget venenatis eros. Cras euismod eget justo id sodales. Vestibulum a ullamcorper turpis. Suspendisse potenti. Curabitur ac condimentum dui.

Donec mollis leo lorem, vel dictum nisi efficitur id. Praesent mollis vel ante efficitur placerat. Nunc nec eros ac ex laoreet tristique non ac neque. Cras felis elit, eleifend eget nisl aliquet, maximus maximus justo.
