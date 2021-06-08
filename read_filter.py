import json 

json_textexteral = '''{
    "records": [
        {
            "schedulerType": "JOBP",
            "calendarDay": "DAILY",
            "jobName": "JOBP.INTLMXECOMM.MX.INC.ECOMM.TABLES.OMS.MASTER.WORKFLOW",
            "activationTime": "2021-06-06T00:02:34Z",
            "actualStartTime": "2021-06-06T00:02:38Z",
            "actualEndTime": "2021-06-06T11:42:22Z",
            "endedOKCount": 0,
            "staus": {
                "statusCode": "1900",
                "statusDescription": "Completed Successfully"
            }
        },
        {
            "schedulerType": "JOBP",
            "calendarDay": "DAILY",
            "jobName": "JOBP.INTLMXECOMM.MX.INC.ECOMM.TABLES.OMS.MASTER.WORKFLOW",
            "activationTime": "2021-06-06T11:42:35Z",
            "actualStartTime": "2021-06-06T11:42:52Z",
            "actualEndTime": "2021-06-06T13:50:01Z",
            "endedOKCount": 0,
            "staus": {
                "statusCode": "1900",
                "statusDescription": "Completed Successfully"
            }
        },
        {
            "schedulerType": "JOBP",
            "calendarDay": "DAILY",
            "jobName": "JOBP.INTLMXECOMM.MX.INC.ECOMM.TABLES.OMS.MASTER.WORKFLOW",
            "activationTime": "2021-06-06T13:50:34Z",
            "actualStartTime": "2021-06-06T13:50:38Z",
            "actualEndTime": "2021-06-06T16:07:24Z",
            "endedOKCount": 0,
            "staus": {
                "statusCode": "1900",
                "statusDescription": "Completed Successfully"
            }
        },
        {
            "schedulerType": "JOBP",
            "calendarDay": "DAILY",
            "jobName": "JOBP.INTLMXECOMM.MX.INC.ECOMM.TABLES.OMS.MASTER.WORKFLOW",
            "activationTime": "2021-06-06T16:10:34Z",
            "actualStartTime": "2021-06-06T16:10:39Z",
            "endedOKCount": 0,
            "staus": {
                "statusCode": "0",
                "statusDescription": "Running"
            }
        }
    ]
    }
    '''

def validateError(json_text):
    json_format = json.loads(json_text)
    list = []
    for records in json_format['records']:
        jobName = records['jobName']
        statusDesc = records['staus']['statusDescription']
        data = statusDesc
        list.append(data)
    if('Running' in list):
        print("Running Job: {0} Tiene que enviar correo".format(jobName))
        #PUSH STATUS
    elif('Error' in list): 
        print("Error Job: {0} Tiene que enviar correo".format(jobName))
    elif('Blocked' in list): 
        print("Blocked Job: {0} Tiene que enviar correo".format(jobName))
    


validateError(json_textexteral)