from qiskit.providers.backend import BackendV2
from qiskit.transpiler import Target
from MikokJob import MikokJob

class MikokBackend(BackendV2):

    def __init__(self,provider):
        super().__init__(name = 'mikok_simulator', 
        provider=provider)
        self.target = Target('Target of backend')
        # self._configuration = BackendConfiguration.from_dict({
        # 'backend_name': 'mikok_simulator',
        # 'backend_version': '0.0.1',
        # 'url': self.url,
        # 'simulator': True,
        # 'local': False,
        # 'coupling_map': None,
        # 'description': 'AQT trapped-ion device simulator',
        # 'basis_gates': ['rx', 'ry', 'rz', 'r', 'rxx'],
        # 'memory': False,
        # 'n_qubits': 11,gti
        # 'conditional': False,
        # 'max_shots': 200,
        # 'max_experiments': 1,
        # 'open_pulse': False,
        # 'gates': [
        #         {
        #             'name': 'TODO',
        #             'parameters': [],
        #             'qasm_def': 'TODO'
        #         }
        #     ]
        # })
    #     self._target = Target("Target from ")
    def _default_options(cls):
        """Return the default options

        This method will return a :class:`qiskit.providers.Options`
        subclass object that will be used for the default options. These
        should be the default parameters to use for the options of the
        backend.

        Returns:
            qiskit.providers.Options: A options object with
                default values set
        """
        pass

    def max_circuits(self):
        """The maximum number of circuits (or Pulse schedules) that can be
        run in a single job.

        If there is no limit this will return None
        """
    
    def target(self):
        """A :class:`qiskit.transpiler.Target` object for the backend.

        :rtype: Target
        """
        pass

    def run(self, run_input, **options):
        """Run on the backend.

        This method returns a :class:`~qiskit.providers.Job` object
        that runs circuits. Depending on the backend this may be either an async
        or sync call. It is at the discretion of the provider to decide whether
        running should block until the execution is finished or not: the Job
        class can handle either situation.

        Args:
            run_input (QuantumCircuit or Schedule or ScheduleBlock or list): An
                individual or a list of
                :class:`~qiskit.circuits.QuantumCircuit,
                :class:`~qiskit.pulse.ScheduleBlock`, or
                :class:`~qiskit.pulse.Schedule` objects to run on the backend.
            options: Any kwarg options to pass to the backend for running the
                config. If a key is also present in the options
                attribute/object then the expectation is that the value
                specified will be used instead of what's set in the options
                object.
        Returns:
            Job: The job object for the run
        """
        job = MikokJob(self,1 )
        return job