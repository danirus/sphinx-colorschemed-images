CS Figure with Language
=======================

Here there are two examples of use of the ``cs_figure`` directive. One with the file extension (``.png``) and the other with an asterisk (``.*``).

With extension
##############

The figure here has the URI ``img/balloon.png``, but the actual file is called ``img/balloon.en.png``:

.. code-block:: reStructuredText

   .. cs_figure:: img/balloon.png
      :alt: A balloon icon
      :align: right
      :width: 200

      A balloon icon

.. cs_figure:: img/balloon.png
   :alt: A balloon icon
   :align: right
   :width: 200

   A balloon icon

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus pretium blandit tortor vitae efficitur. Vestibulum eget venenatis eros. Cras euismod eget justo id sodales. Vestibulum a ullamcorper turpis. Suspendisse potenti. Curabitur ac condimentum dui.

Donec mollis leo lorem, vel dictum nisi efficitur id. Praesent mollis vel ante efficitur placerat. Nunc nec eros ac ex laoreet tristique non ac neque. Cras felis elit, eleifend eget nisl aliquet, maximus maximus justo.

With an asterisk
################

The figure in this example has the URI ``img/balloon.*``, but the actual file is called ``img/balloon.en.png``:

.. code-block:: reStructuredText

   .. cs_figure:: img/balloon.*
      :alt: A balloon icon
      :align: right
      :width: 200

      A balloon icon

.. cs_figure:: img/balloon.*
   :alt: A balloon icon
   :align: right
   :width: 200

   A balloon icon

Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Vivamus pretium blandit tortor vitae efficitur. Vestibulum eget venenatis eros. Cras euismod eget justo id sodales. Vestibulum a ullamcorper turpis. Suspendisse potenti. Curabitur ac condimentum dui.

Donec mollis leo lorem, vel dictum nisi efficitur id. Praesent mollis vel ante efficitur placerat. Nunc nec eros ac ex laoreet tristique non ac neque. Cras felis elit, eleifend eget nisl aliquet, maximus maximus justo.