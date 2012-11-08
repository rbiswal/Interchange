
mdn = context.getVariable('request.queryparam.mdn');

if (mdn == '9403511193') {
	context.setVariable('ix.carrier', 'ATT');
} else if (mdn == '4088289456' || mdn == '2223339998' || mdn == '9089475790') {
	context.setVariable('ix.carrier', 'VZ');
} else {
	context.setVariable('ix.carrier', 'OT');
}
