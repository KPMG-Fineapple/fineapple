import { Injectable, Logger } from '@nestjs/common';
import { spawn } from 'child_process';

@Injectable()
export class PowerGenerationService {
  private logger = new Logger('PowerGenerationService');

  getPowerGeneration(address: string) {
    const process = spawn('python3', ['../AI/power-generation-model.py']);

    process.stdout.on('data', function (data) {
      const result = JSON.parse(data.toString());
      Logger.debug('GET DATA :' + data.toString());
      return result;
    });

    process.stderr.on('data', function (data) {
      Logger.error(data.toString());
    });
  }
}
