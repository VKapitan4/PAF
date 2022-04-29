class Particle {
    public:
        Particle(float x0, float y0, float v0, float kut);
        ~Particle();

        float range();
        float time();

    private:
        void move();
        float _dt;
        float _x;
        float _y;
        float _vx;
        float _vy;
        float _ax;
        float _ay;
        float _y0;

};