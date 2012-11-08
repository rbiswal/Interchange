flow.setVariable("flow.testvar3","new value 3");
if(flow.getVariable("request.header.response.code")):
	flow.setVariable("status.code",flow.getVariable("request.header.response.code"));
else:
	flow.setVariable("status.code","500");
