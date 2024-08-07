# This code is part of Qiskit.
#
# (C) Copyright IBM 2022, 2024
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
=====================================================
Primitive options (:mod:`qiskit_ibm_runtime.options`)
=====================================================

.. currentmodule:: qiskit_ibm_runtime.options

Options that can be passed to the Qiskit Runtime primitives.

V2 Primitives
=============

``SamplerV2`` and ``EstimatorV2`` each have their own options. You can use the
``options`` attribute to set the options. For example::

   from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2

   service = QiskitRuntimeService()
   backend = service.least_busy(operational=True, simulator=False)
   estimator = EstimatorV2(backend=backend)
   estimator.options.resilience_level = 1

You can also use the ``update()`` method to do bulk update. For example::

   from qiskit_ibm_runtime import QiskitRuntimeService, EstimatorV2

   service = QiskitRuntimeService()
   backend = service.least_busy(operational=True, simulator=False)
   estimator = EstimatorV2(backend=backend)
   estimator.options.update(resilience_level=1)

Refer to :class:`SamplerOptions` and :class:`EstimatorOptions` for V2 Sampler and
V2 Estimator options, respectively.

.. note::
   If an option is not specified, the server default value is used. The
   default values are subject to change. Refer to this current module's documentation
   for the latest defaults.


V1 Primitives
=============

The :class:`Options` class encapsulates all the options you can specify
when invoking a V1 primitive. It includes frequently used options,
such as ``optimization_level`` and ``resilience_level`` as well as
sub-categories, such as ``transpilation`` and ``execution``.
You can use auto-complete to easily find the options inside each
sub-category, for example::

   from qiskit_ibm_runtime.options import Options

   options = Options()
   options.transpilation.initial_layout = [0, 1, 2, 3]  # This an be done using auto-complete

You can also pass dictionaries to each sub-category, for example::

   from qiskit_ibm_runtime.options import Options

   options = Options(transpilation={"initial_layout": [0, 1, 2, 3]})


Classes
=======

Base primitive options
----------------------

.. autosummary::
   :toctree: ../stubs/

   EstimatorOptions
   SamplerOptions
   Options


Suboptions for V2 primitives only
---------------------------------

.. autosummary::
   :toctree: ../stubs/

   DynamicalDecouplingOptions
   ResilienceOptionsV2
   LayerNoiseLearningOptions
   MeasureNoiseLearningOptions
   PecOptions
   ZneOptions
   TwirlingOptions
   ExecutionOptionsV2
   SamplerExecutionOptionsV2


Suboptions for both V1 and V2 primitives
----------------------------------------

.. autosummary::
   :toctree: ../stubs/

   EnvironmentOptions
   SimulatorOptions


Suboptions for V1 primitives only
---------------------------------

.. autosummary::
   :toctree: ../stubs/

   TranspilationOptions
   ExecutionOptions
   ResilienceOptions

"""

from .environment_options import EnvironmentOptions
from .execution_options import ExecutionOptions
from .execution_options import ExecutionOptionsV2
from .noise_learner_options import NoiseLearnerOptions
from .options import Options, OptionsV2
from .simulator_options import SimulatorOptions
from .transpilation_options import TranspilationOptions
from .resilience_options import ResilienceOptions
from .resilience_options import ResilienceOptionsV2
from .twirling_options import TwirlingOptions
from .estimator_options import EstimatorOptions
from .sampler_options import SamplerOptions
from .dynamical_decoupling_options import DynamicalDecouplingOptions
from .layer_noise_learning_options import LayerNoiseLearningOptions
from .measure_noise_learning_options import MeasureNoiseLearningOptions
from .pec_options import PecOptions
from .zne_options import ZneOptions
from .sampler_execution_options import SamplerExecutionOptionsV2
