import { Injectable, Logger } from '@nestjs/common';
import { spawnSync } from 'child_process';

@Injectable()
export class PowerGenerationService {
  private logger = new Logger('PowerGenerationService');

  getPowerGeneration() {
    const process = spawnSync('python3', ['../AI/power-generation-model.py']);
    const result = JSON.parse(
      Buffer.from(process.stdout.toJSON().data).toString(),
    );
    return result;
  }
}
