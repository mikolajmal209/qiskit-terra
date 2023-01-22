from qiskit.providers.job import JobV1 as Job 


class MikokJob(Job):



    
    def submit(self):
        """Submit the job to the backend for execution."""
        print('submited')

    def result(self):
        """Return the results of the job."""


        return {'0': '100','1':'200'}

    def cancel(self):
        """Attempt to cancel the job."""
        raise NotImplementedError

    def status(self):
        """Return the status of the job, among the values of ``JobStatus``."""
        pass
